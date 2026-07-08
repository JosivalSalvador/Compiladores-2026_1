# Autor: Josival Salvador Monteiro Júnior
# Trabalho 09 - Geração de Código Assembly do EduMIPS64
#
# Gera Assembly EduMIPS64 a partir do código de três endereços (TAC).
# O TAC é lido como texto, linha a linha, com um parser simples escrito à mão.
#
# Formato de entrada aceito (produzido pelo tac_generator.py):
#
#   global_counter = 0     (atribuicao solta -- inicializacao de global)
#
#   func nome, N:
#       <instrucoes indentadas>
#   endfunc
#
#   L1:
#       t1 = a + b        (atribuicao: destino = operando op operando)
#       t2 = a            (copia simples: destino = operando)
#       t3 = -a           (negacao: destino = - operando)
#       t3 = !a           (negacao logica: destino = ! operando)
#       t4 = call f, 2    (chamada: destino = call nome, n_argumentos)
#       if a goto L1      (desvio condicional)
#       goto L2           (desvio incondicional)
#       print a           (impressao de um operando)
#       print "texto"     (impressao de uma string literal)
#       print "x=", a     (impressao mista, varios argumentos separados por virgula)
#       param a           (empilha argumento antes de uma chamada)
#       return a          (retorno de valor)
#
# Um ';' opcional no fim de qualquer instrucao e ignorado. Comentarios com '#'
# e linhas em branco sao ignorados.
#
# Convencoes de geracao:
#   - toda variável de uma função mora em um slot de 8 bytes no frame dessa
#     função (nunca em registrador fixo entre uma instrução e outra);
#   - $t8/$t9: registradores de trabalho transitórios; $t6 (=r14): bloco de
#     parâmetros do syscall 5;
#   - globais moram em .data, endereçadas pelo próprio rótulo;
#   - variável global com inicializador ('int x = 5;') vira uma atribuição
#     solta no TAC, fora de qualquer 'func'; essas atribuições são emitidas
#     como instruções '.code' logo antes de 'main:' (ver
#     compile_global_inits). Sem inicializador, nada extra é gerado -- o
#     '.space' de cada global já nasce zerado;
#   - pilha reservada em .data (STACK_SIZE bytes); $sp inicializado para o
#     topo dela no começo de 'main' (o simulador começa com $sp = 0, então
#     sem isso qualquer 'daddi $sp,$sp,-N' gera endereço de memória negativo);
#   - parâmetros 0-3 em $a0-$a3, parâmetro 4+ na pilha, retorno em $v0,
#     $ra salvo no frame de qualquer função que faça alguma chamada;
#   - 'main' nunca salva $ra; cada 'return' de main vira 'syscall 0';
#   - epílogo de fim de função só é emitido se o corpo não terminar em
#     'return' (evita duplicar syscall 0/jr $ra quando o último statement já
#     é um 'return');
#   - */÷/% usam dmult/ddiv + mflo/mfhi; goto incondicional usa 'j';
#   - rótulos do TAC são prefixados com o nome da função (namespace único).
#
# O item solto "_main_result = call main, 0" que o tac_generator.py sempre
# emite ao final tambem chega como instrucao solta (fora de qualquer func),
# junto com as inicializacoes de global -- mas e filtrado em
# compile_global_inits() pelo formato do rhs (so 'copy' vira instrucao de
# verdade; 'call' e ignorado, mesmo comportamento documentado desde sempre
# aqui: o bloco 'func main, 0:' ja vira o 'main:' do Assembly diretamente).

import re


SCRATCH = ('$t8', '$t9')            # registradores de trabalho transitorios
PARAM_REGS = ('$a0', '$a1', '$a2', '$a3')
SYSCALL5_ARG_REG = '$t6'            # == r14 (obrigatorio p/ syscall 5, resumoComp pdf1)

STACK_SIZE = 2048                   # bytes reservados p/ pilha (mesmo tamanho de exemplo6/7.asm)
STACK_BOTTOM_LABEL = '_stack_bottom'
STACK_TOP_LABEL = '_stack_top'

# CORREÇÃO: '%' (módulo) estava faltando nesta lista. Sem ele,
# _split_binary_rhs() nunca reconhecia 'x % 4' como uma operação binária,
# e a linha inteira caia no caminho de 'copy' (operando único) em
# _parse_rhs() -- gerando um Operand cujo texto era a string inteira
# "x % 4", que nunca existe em 'offsets', quebrando a leitura de módulo em
# qualquer contexto (atribuição comum OU dentro de %=, já que ambos passam
# pela mesma rota). Único ponto de correção deste bug.
BIN_OPS = ('>=', '<=', '==', '!=', '&&', '||', '+', '-', '*', '/', '%', '>', '<')
# ^ operadores de 2 caracteres antes dos de 1 caractere, para o rfind() nao
#   achar soh a metade de '>=' (por exemplo) e cortar o texto no lugar errado.


# =====================================================================
# Estruturas intermediarias (equivalentes aos *Context do ANTLR antigo)
# =====================================================================

class Operand:
    """Um operando de uma instrucao TAC: ou um identificador (ID) ou uma
    constante inteira (INT). Espelha a regra 'operand: ID | INT' do TAC.g4."""

    __slots__ = ('text', 'is_int')

    def __init__(self, text):
        self.text = text
        self.is_int = bool(re.fullmatch(r'-?[0-9]+', text))

    def __repr__(self):
        return f"Operand({self.text!r})"


class Stmt:
    """Uma instrucao TAC ja classificada. 'kind' indica qual das alternativas
    de 'stmt' (TAC.g4) esta instrucao representa, e 'data' guarda os campos
    especificos dessa alternativa -- no mesmo papel que os *Context tinham."""

    __slots__ = ('kind', 'data')

    def __init__(self, kind, **data):
        self.kind = kind
        self.data = data

    def __repr__(self):
        return f"Stmt({self.kind}, {self.data})"


class ParseError(RuntimeError):
    """Erro de leitura do TAC de entrada -- nao deveria ocorrer para TAC
    gerado pelo tac_generator.py; existe para apontar rapidamente qualquer
    incompatibilidade caso o formato de entrada mude no futuro."""
    pass


# =====================================================================
# Parser de texto do TAC (substitui TACLexer/TACParser/TACVisitor)
# =====================================================================

def _strip_comment_and_semicolon(line):
    # remove comentario '# ...' (TAC.g4: COMMENT: '#' ~[\r\n]* -> skip),
    # respeitando strings entre aspas (uma string de print poderia conter '#')
    in_string = False
    for i, ch in enumerate(line):
        if ch == '"':
            in_string = not in_string
        elif ch == '#' and not in_string:
            line = line[:i]
            break
    line = line.strip()
    if line.endswith(';'):
        line = line[:-1].strip()
    return line


def _split_top_level_commas(text):
    """Separa por virgula, respeitando strings entre aspas (usado em
    printStat, que aceita varios printArg separados por ',')."""
    parts, current, in_string = [], [], False
    for ch in text:
        if ch == '"':
            in_string = not in_string
            current.append(ch)
        elif ch == ',' and not in_string:
            parts.append(''.join(current).strip())
            current = []
        else:
            current.append(ch)
    parts.append(''.join(current).strip())
    return parts


def _parse_print_arg(text):
    text = text.strip()
    if text.startswith('"') and text.endswith('"'):
        return ('string', text[1:-1])
    return ('operand', Operand(text))


def _split_binary_rhs(text):
    """Tenta separar 'texto' em (esquerda, operador, direita) usando os
    operadores de OP (TAC.g4), varrendo cada operador pela DIREITA do texto
    (rfind) -- mais seguro contra um operando negativo do lado direito, como
    em 't1 = a > -5' (nao deve cortar no '-' de '-5')."""
    for op in BIN_OPS:
        idx = text.rfind(op)
        if idx <= 0:
            continue
        left = text[:idx].strip()
        right = text[idx + len(op):].strip()
        if left and right:
            return left, op, right
    return None


def parse_tac(source: str):
    """Le o texto do TAC e devolve (functions, global_inits):
      - functions: {nome_funcao: {'n_params', 'body': [Stmt,...], 'labels': {rotulo: indice}}}
      - global_inits: [Stmt, ...] -- instrucoes soltas fora de qualquer 'func'
        (inicializacao de variaveis globais, tipo 'global_counter = 0'; o
        kickoff '_main_result = call main, 0' tambem cai aqui, mas e
        filtrado depois em MipsGenerator.compile_global_inits pelo formato
        do rhs -- so 'copy' vira instrucao de verdade)."""

    functions = {}
    global_inits = []
    current_name = None
    current_n_params = None
    current_body = None
    current_labels = None

    func_header_re = re.compile(r'^func\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*,\s*([0-9]+)\s*:$')
    label_re = re.compile(r'^([a-zA-Z_][a-zA-Z_0-9]*)\s*:$')

    for raw_line in source.splitlines():
        line = _strip_comment_and_semicolon(raw_line)
        if not line:
            continue

        # ---- fim de funcao ----
        if line == 'endfunc':
            if current_name is None:
                raise ParseError("'endfunc' encontrado fora de qualquer 'func'")
            functions[current_name] = {
                'n_params': current_n_params,
                'body': current_body,
                'labels': current_labels,
            }
            current_name = None
            continue

        # ---- inicio de funcao ----
        m = func_header_re.match(line)
        if m:
            if current_name is not None:
                raise ParseError(f"'func {m.group(1)}' iniciada antes de 'endfunc' de '{current_name}'")
            current_name = m.group(1)
            current_n_params = int(m.group(2))
            current_body = []
            current_labels = {}
            continue

        # ---- instrucao solta fora de qualquer func (inicializacao de global, ou o kickoff) ----
        if current_name is None:
            global_inits.append(_parse_stmt(line))
            continue

        # ---- rotulo sozinho ("L3:") ----
        m = label_re.match(line)
        if m:
            current_labels[m.group(1)] = len(current_body)
            continue

        # ---- demais instrucoes ----
        current_body.append(_parse_stmt(line))

    if current_name is not None:
        raise ParseError(f"'func {current_name}' nao foi fechada com 'endfunc'")

    return functions, global_inits


def _parse_stmt(line):
    if line.startswith('if ') and ' goto ' in line:
        rest = line[3:]
        cond_text, _, label = rest.partition(' goto ')
        return Stmt('ifGoto', operand=Operand(cond_text.strip()), label=label.strip())

    if line.startswith('goto '):
        return Stmt('goto', label=line[5:].strip())

    if line.startswith('print '):
        args_text = line[6:].strip()
        args = [_parse_print_arg(a) for a in _split_top_level_commas(args_text)]
        return Stmt('print', args=args)

    if line.startswith('param '):
        return Stmt('param', operand=Operand(line[6:].strip()))

    if line.startswith('return '):
        return Stmt('return', operand=Operand(line[7:].strip()))

    if '=' in line:
        target, _, rhs_text = line.partition('=')
        target = target.strip()
        rhs_text = rhs_text.strip()
        return Stmt('assign', target=target, rhs=_parse_rhs(rhs_text))

    raise ParseError(f"instrucao TAC nao reconhecida: {line!r}")


def _parse_rhs(text):
    if text.startswith('call '):
        rest = text[5:].strip()
        name, _, n_text = rest.partition(',')
        return ('call', name.strip(), int(n_text.strip()))

    if text.startswith('!'):
        return ('not', Operand(text[1:].strip()))

    if text.startswith('-') and not re.fullmatch(r'-[0-9]+', text):
        # '-a' (negacao) vs '-5' (constante negativa): so trata como negRhs
        # se o que sobra depois do '-' NAO for puramente numerico
        return ('neg', Operand(text[1:].strip()))

    split = _split_binary_rhs(text)
    if split:
        left, op, right = split
        return ('binary', Operand(left), op, Operand(right))

    return ('copy', Operand(text))


# =====================================================================
# Gerador de Assembly (mesma logica de traducao de antes, agora consumindo
# as estruturas Stmt/Operand em vez de *Context do ANTLR)
# =====================================================================

class MipsGenerator:

    def __init__(self, global_names):
        self.global_names = set(global_names)

        self.functions = {}          # nome -> {'n_params', 'body': [Stmt,...], 'labels': {label: idx}}
        self.global_inits = []        # Stmt(s) fora de qualquer func (inicializacao de globais)
        self.out = []                 # linhas de Assembly ja geradas (.code)
        self.string_literals = []     # [(rotulo, '"texto com aspas"'), ...]
        self.print_blocks = []        # [(rotulo, tamanho_em_bytes), ...]
        self.pending_params = []      # fila de operandos empilhados por 'param' (por funcao)
        self._str_lit_count = 0

    # ---------- ponto de entrada ----------

    def generate(self, tac_source: str) -> str:
        self.functions, self.global_inits = parse_tac(tac_source)

        if 'main' not in self.functions:
            raise RuntimeError("TAC de entrada nao possui 'func main, 0:'")

        self.compile_global_inits()
        self.compile_function('main', is_main=True)
        for name in self.functions:
            if name != 'main':
                self.compile_function(name, is_main=False)

        data = ['        .data']
        # CORRECAO 1: area de pilha, para $sp ter um endereco POSITIVO valido
        # antes do primeiro 'daddi $sp,$sp,-N' -- sem isso $sp comeca em 0 e
        # qualquer frame gera endereco negativo (AddressErrorException).
        data.append(f"{STACK_BOTTOM_LABEL}:  .space {STACK_SIZE}")
        data.append(f"{STACK_TOP_LABEL}:")
        for g in sorted(self.global_names):
            data.append(f"{g}:  .space 8")
        for label, text in self.string_literals:
            data.append(f"{label}:  .asciiz {text}")
        for label, size in self.print_blocks:
            data.append(f"{label}:  .space {size}")
        data.append('')

        code = ['        .code'] + self.out
        return "\n".join(data + code)

    def compile_global_inits(self):
        """Emite, antes de 'main:', a inicializacao de variaveis globais que
        tem '= valor' na declaracao -- ex: 'int global_counter = 0;' vira
        'daddi $t8,$zero,0' + 'sd $t8,global_counter($zero)' logo no comeco
        do .code, antes de qualquer label. Globais sem inicializador nao
        aparecem aqui (o .space da secao .data ja nasce zerado). O kickoff
        '_main_result = call main, 0' que o tac_generator.py sempre
        acrescenta tambem chega em self.global_inits, mas tem rhs 'call'
        (nao 'copy') e por isso e ignorado aqui."""
        for stmt in self.global_inits:
            if stmt.kind == 'assign' and stmt.data['rhs'][0] == 'copy':
                self.compile_assign(stmt.data['target'], stmt.data['rhs'], offsets={})

    # ---------- coleta de variaveis de UMA funcao (1a passada) ----------

    def collect_vars(self, func_info):
        """Devolve, na ordem de primeira aparicao, todo identificador local
        (parametro, temporario ou variavel) referenciado no corpo -- ignora
        globais, rotulos e literais. Tambem informa se a funcao faz alguma
        chamada (usado para decidir se precisa salvar $ra)."""
        n_params = func_info['n_params']
        var_list = [f"p{i}" for i in range(n_params)]
        seen = set(var_list)
        calls_something = False

        def see(name):
            if name not in self.global_names and name not in seen:
                seen.add(name)
                var_list.append(name)

        def visit_operand(op):
            if not op.is_int:
                see(op.text)

        for stmt in func_info['body']:
            if stmt.kind == 'assign':
                see(stmt.data['target'])
                rhs = stmt.data['rhs']
                tag = rhs[0]
                if tag == 'call':
                    calls_something = True
                elif tag == 'binary':
                    _, left, _op, right = rhs
                    visit_operand(left)
                    visit_operand(right)
                elif tag in ('neg', 'not', 'copy'):
                    visit_operand(rhs[1])
            elif stmt.kind == 'ifGoto':
                visit_operand(stmt.data['operand'])
            elif stmt.kind == 'print':
                for kind, val in stmt.data['args']:
                    if kind == 'operand':
                        visit_operand(val)
            elif stmt.kind == 'param':
                visit_operand(stmt.data['operand'])
            elif stmt.kind == 'return':
                visit_operand(stmt.data['operand'])

        return var_list, calls_something

    # ---------- geracao de UMA funcao ----------

    def compile_function(self, name, is_main):
        func_info = self.functions[name]
        var_list, calls_something = self.collect_vars(func_info)

        # 'main' nunca salva $ra: nunca faz jr $ra (quem "retorna" de main e
        # o syscall 0 que encerra o simulador) -- ver convencao 6
        ra_slot = 8 if (calls_something and not is_main) else 0
        offsets = {v: ra_slot + 8 * i for i, v in enumerate(var_list)}
        frame_size = ra_slot + 8 * len(var_list)

        labels_at_index = {}
        for label_name, idx in func_info['labels'].items():
            labels_at_index.setdefault(idx, []).append(label_name)

        self.pending_params = []
        # CORRECAO 2: flag para saber se o ultimo statement emitido ja foi um
        # 'return' (e portanto ja gerou seu proprio epilogo) -- usado no final
        # desta funcao para decidir se a rede de seguranca ainda e necessaria.
        self._last_stmt_was_return = False

        self._emit(f"{name}:")

        if is_main:
            # CORRECAO 1: inicializa $sp para o topo da area de pilha reservada
            # em .data ANTES de qualquer 'daddi $sp,$sp,-N' -- sem isso $sp
            # comeca em 0 (padrao do simulador) e vira negativo no primeiro
            # frame. So precisa ser feito uma vez, no comeco de 'main'.
            self._emit(f"daddi   $sp, $zero, {STACK_TOP_LABEL}", "inicializa a pilha")

        if frame_size > 0:
            self._emit(f"daddi   $sp, $sp, -{frame_size}", f"abre o frame de {name} ({frame_size} bytes)")

        # parametros vindos da pilha (indice >= 4): leem-se ANTES de qualquer
        # outro uso de $sp -- estao a 'frame_size' bytes ACIMA do novo $sp,
        # que e onde o CHAMADOR os deixou empilhados
        n_params = func_info['n_params']
        for i in range(4, n_params):
            caller_offset = frame_size + 8 * (i - 4)
            self._emit(f"ld      $t9, {caller_offset}($sp)", f"le parametro p{i} empilhado pelo chamador")
            self._emit(f"sd      $t9, {offsets['p' + str(i)]}($sp)")

        # parametros vindos de registrador ($a0-$a3)
        for i in range(min(4, n_params)):
            self._emit(f"sd      {PARAM_REGS[i]}, {offsets['p' + str(i)]}($sp)", f"guarda parametro p{i}")

        if ra_slot:
            self._emit("sd      $ra, 0($sp)", "salva endereco de retorno")

        for idx, stmt in enumerate(func_info['body']):
            for label_name in labels_at_index.get(idx, []):
                self._emit(f"{name}_{label_name}:")
            self.compile_stmt(stmt, name, offsets, frame_size, ra_slot, is_main)

        for label_name in labels_at_index.get(len(func_info['body']), []):
            self._emit(f"{name}_{label_name}:")

        # CORRECAO 2: rede de seguranca -- so emite se o ultimo statement do
        # corpo NAO ja foi um 'return' (que ja emitiu seu proprio epilogo).
        # Na pratica, com o tac_generator.py atual (que sempre fecha toda
        # funcao com 'return' explicito), este bloco normalmente fica
        # inalcancavel -- mas continua aqui como rede de seguranca real para
        # qualquer TAC que porventura nao termine em 'return'.
        if not self._last_stmt_was_return:
            if is_main:
                self._emit("syscall 0", "encerra o simulador (fim de main)")
            else:
                self._emit_return_epilogue(frame_size, ra_slot)

        self._emit("")

    def _emit_return_epilogue(self, frame_size, ra_slot):
        if ra_slot:
            self._emit("ld      $ra, 0($sp)", "restaura endereco de retorno")
        if frame_size:
            self._emit(f"daddi   $sp, $sp, {frame_size}", "fecha o frame")
        self._emit("jr      $ra")

    # ---------- traducao de um statement ----------

    def compile_stmt(self, stmt, func_name, offsets, frame_size, ra_slot, is_main):
        # CORRECAO 2: registra se ESTE statement e um 'return' -- usado pelo
        # chamador (compile_function) para decidir se a rede de seguranca
        # final ainda e necessaria. Qualquer outro tipo de statement zera a
        # flag (ela so deve valer True se o ULTIMO statement do corpo foi
        # exatamente um 'return').
        self._last_stmt_was_return = (stmt.kind == 'return')

        if stmt.kind == 'assign':
            self.compile_assign(stmt.data['target'], stmt.data['rhs'], offsets)
        elif stmt.kind == 'ifGoto':
            reg = self.load_operand(stmt.data['operand'], offsets, SCRATCH[0])
            self._emit(f"bne     {reg}, $zero, {func_name}_{stmt.data['label']}")
        elif stmt.kind == 'goto':
            self._emit(f"j       {func_name}_{stmt.data['label']}")
        elif stmt.kind == 'print':
            self.compile_print(stmt.data['args'], offsets)
        elif stmt.kind == 'param':
            self.pending_params.append(stmt.data['operand'])
        elif stmt.kind == 'return':
            self.load_operand(stmt.data['operand'], offsets, '$v0')
            if is_main:
                self._emit("syscall 0", "encerra o simulador")
            else:
                self._emit_return_epilogue(frame_size, ra_slot)

    def compile_assign(self, target, rhs, offsets):
        tag = rhs[0]

        if tag == 'call':
            _, callee, n_args = rhs
            self.compile_call(callee, n_args, target, offsets)
            return

        if tag == 'binary':
            _, left_op, op_symbol, right_op = rhs
            left = self.load_operand(left_op, offsets, SCRATCH[0])
            right = self.load_operand(right_op, offsets, SCRATCH[1])
            self.compile_binary_op(op_symbol, SCRATCH[0], left, right)
            self.store_result(SCRATCH[0], target, offsets)
            return

        if tag == 'neg':
            r = self.load_operand(rhs[1], offsets, SCRATCH[0])
            self._emit(f"dsubu   {SCRATCH[0]}, $zero, {r}")
            self.store_result(SCRATCH[0], target, offsets)
            return

        if tag == 'not':
            r = self.load_operand(rhs[1], offsets, SCRATCH[0])
            self._emit(f"sltiu   {SCRATCH[0]}, {r}, 1")
            self.store_result(SCRATCH[0], target, offsets)
            return

        if tag == 'copy':
            r = self.load_operand(rhs[1], offsets, SCRATCH[0])
            self.store_result(r, target, offsets)
            return

    def compile_binary_op(self, op, dest, left_reg, right_reg):
        if op == '+':
            self._emit(f"daddu   {dest}, {left_reg}, {right_reg}")
        elif op == '-':
            self._emit(f"dsubu   {dest}, {left_reg}, {right_reg}")
        elif op == '*':
            self._emit(f"dmult   {left_reg}, {right_reg}")
            self._emit(f"mflo    {dest}")
        elif op == '/':
            self._emit(f"ddiv    {left_reg}, {right_reg}")
            self._emit(f"mflo    {dest}")
        elif op == '%':
            self._emit(f"ddiv    {left_reg}, {right_reg}")
            self._emit(f"mfhi    {dest}")
        elif op == '<':
            self._emit(f"slt     {dest}, {left_reg}, {right_reg}")
        elif op == '>':
            self._emit(f"slt     {dest}, {right_reg}, {left_reg}")
        elif op == '<=':
            self._emit(f"slt     {dest}, {right_reg}, {left_reg}")
            self._emit(f"xori    {dest}, {dest}, 1")
        elif op == '>=':
            self._emit(f"slt     {dest}, {left_reg}, {right_reg}")
            self._emit(f"xori    {dest}, {dest}, 1")
        elif op == '==':
            self._emit(f"xor    {dest}, {left_reg}, {right_reg}")
            self._emit(f"sltiu   {dest}, {dest}, 1")
        elif op == '!=':
            self._emit(f"xor    {dest}, {left_reg}, {right_reg}")
            self._emit(f"sltu    {dest}, $zero, {dest}")
        elif op == '&&':
            self._emit(f"sltu    {left_reg}, $zero, {left_reg}")
            self._emit(f"sltu    {right_reg}, $zero, {right_reg}")
            self._emit(f"and     {dest}, {left_reg}, {right_reg}")
        elif op == '||':
            self._emit(f"or      {dest}, {left_reg}, {right_reg}")
            self._emit(f"sltu    {dest}, $zero, {dest}")

    # ---------- chamada de funcao ----------

    def compile_call(self, callee, n_args, target_name, offsets):
        args = self.pending_params[-n_args:] if n_args > 0 else []
        self.pending_params = self.pending_params[:len(self.pending_params) - n_args]

        # 1) os 4 primeiros argumentos vao direto para $a0-$a3
        for i in range(min(4, n_args)):
            self.load_operand(args[i], offsets, PARAM_REGS[i])

        # 2) argumentos extras (indice >= 4): empilha ANTES do jal, desempilha
        #    depois. 'extra_shift' compensa o deslocamento temporario de $sp
        #    para que load_operand continue lendo os slots corretos.
        extra = n_args - 4
        if extra > 0:
            self._emit(f"daddi   $sp, $sp, -{8 * extra}", "empilha parametros extras (5o em diante)")
            for i in range(4, n_args):
                self.load_operand(args[i], offsets, SCRATCH[1], extra_shift=8 * extra)
                self._emit(f"sd      {SCRATCH[1]}, {8 * (i - 4)}($sp)")

        self._emit(f"jal     {callee}")

        if extra > 0:
            self._emit(f"daddi   $sp, $sp, {8 * extra}", "desempilha parametros extras")

        self.store_result('$v0', target_name, offsets)

    # ---------- print (printf) -> syscall 5 ----------

    def compile_print(self, args, offsets):
        fmt_pieces, operand_args = [], []
        for kind, val in args:
            if kind == 'string':
                fmt_pieces.append(val)   # sem aspas; ja vem sem elas de _parse_print_arg
            else:
                fmt_pieces.append('%d')
                operand_args.append(val)
        # o comportamento historico (herdado do TACInterpreterVisitor.py do
        # trabalho 8, que usava print() do Python) sempre acrescenta \n no
        # final -- mantido aqui para o mesmo comportamento observavel
        fmt_text = ''.join(fmt_pieces) + '\\n'

        fmt_label = f"_fmt_{self._str_lit_count}"
        block_label = f"_pblk_{self._str_lit_count}"
        self._str_lit_count += 1
        self.string_literals.append((fmt_label, f'"{fmt_text}"'))
        self.print_blocks.append((block_label, 8 * (1 + len(operand_args))))

        self._emit(f"daddi   $t9, $zero, {block_label}", "endereco do bloco de parametros do print")
        self._emit(f"daddi   $t8, $zero, {fmt_label}")
        self._emit("sd      $t8, 0($t9)", "params[0] = &formato")
        for i, op in enumerate(operand_args):
            reg = self.load_operand(op, offsets, SCRATCH[0])
            self._emit(f"sd      {reg}, {8 * (i + 1)}($t9)", f"params[{i + 1}] = argumento {i}")
        self._emit(f"daddi   {SYSCALL5_ARG_REG}, $zero, {block_label}", "r14 = &bloco de parametros")
        self._emit("syscall 5")

    # ---------- operandos e memoria ----------

    def load_operand(self, op: Operand, offsets, scratch_reg, extra_shift=0):
        """Carrega um operando (variavel local, global ou literal INT) em
        'scratch_reg' e devolve o registrador a usar dali em diante."""
        if op.is_int:
            self._emit(f"daddi   {scratch_reg}, $zero, {op.text}")
            return scratch_reg
        name = op.text
        if name in self.global_names:
            self._emit(f"ld      {scratch_reg}, {name}($zero)")
        else:
            self._emit(f"ld      {scratch_reg}, {offsets[name] + extra_shift}($sp)")
        return scratch_reg

    def store_result(self, src_reg, target_name, offsets):
        if target_name in self.global_names:
            self._emit(f"sd      {src_reg}, {target_name}($zero)")
        else:
            self._emit(f"sd      {src_reg}, {offsets[target_name]}($sp)")

    # ---------- saida ----------

    def _emit(self, instruction, comment=None):
        line = instruction if instruction.endswith(':') else f"        {instruction}"
        if comment:
            line += f"  ; {comment}"
        self.out.append(line)