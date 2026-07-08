from TACParser import TACParser
from TACVisitor import TACVisitor


RETURN_SIGNAL = object()  # sentinela para interromper run() ao encontrar um return


class TACInterpreterVisitor(TACVisitor):

    def __init__(self):
        self.globals = {}
        self.functions = {}
        self.instructions = []
        self.labels = {}
        self.call_stack = []
        self.pending_params = []
        self.return_value = None

    # ---------- ambiente de variaveis (escopo local se houver chamada em andamento) ----------

    def current_scope(self):
        return self.call_stack[-1] if self.call_stack else self.globals

    def get_var(self, name):
        return self.current_scope().get(name, 0)

    def set_var(self, name, value):
        self.current_scope()[name] = value

    def eval_operand(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        return self.get_var(ctx.ID().getText())

    # ---------- fase 1: achatamento do programa em lista de instrucoes + tabela de rotulos ----------
    # goto pode saltar em qualquer direcao, entao nao da pra so percorrer a arvore uma vez

    def visitProg(self, ctx: TACParser.ProgContext):
        for item in ctx.item():
            if item.funcDef():
                self.register_function(item.funcDef())
            else:
                self.flatten_instr(item.instr(), self.instructions, self.labels)
        self.run(self.instructions, self.labels)

    def register_function(self, ctx: TACParser.FuncDefContext):
        name = ctx.ID().getText()
        n_params = int(ctx.INT().getText())
        body = []
        body_labels = {}
        for instr in ctx.instr():
            self.flatten_instr(instr, body, body_labels)
        self.functions[name] = {'n_params': n_params, 'body': body, 'labels': body_labels}

    def flatten_instr(self, ctx: TACParser.InstrContext, out_list, out_labels):
        if ctx.label():
            out_labels[ctx.label().ID().getText()] = len(out_list)
        if ctx.stmt():
            out_list.append(ctx.stmt())

    # ---------- fase 2: execucao com ponteiro de instrucao (pc) ----------

    MAX_STEPS = 1_000_000  # protege contra codigo de entrada com loop infinito

    def run(self, instructions, labels):
        pc = 0
        steps = 0
        while pc < len(instructions):
            steps += 1
            if steps > self.MAX_STEPS:
                raise RuntimeError(f"limite de {self.MAX_STEPS} instrucoes excedido (possivel loop infinito)")
            stmt = instructions[pc]
            jump = self.exec_stmt(stmt)
            if jump is RETURN_SIGNAL:
                return
            if jump is not None:
                if jump not in labels:
                    raise RuntimeError(f"rotulo '{jump}' nao definido")
                pc = labels[jump]
            else:
                pc += 1

    def exec_stmt(self, ctx: TACParser.StmtContext):
        if ctx.assign():
            self.exec_assign(ctx.assign())
        elif ctx.ifGoto():
            return self.exec_if_goto(ctx.ifGoto())
        elif ctx.goto():
            return ctx.goto().ID().getText()
        elif ctx.printStat():
            self.exec_print(ctx.printStat())
        elif ctx.paramStat():
            self.pending_params.append(self.eval_operand(ctx.paramStat().operand()))
        elif ctx.returnStat():
            self.return_value = self.eval_operand(ctx.returnStat().operand())
            return RETURN_SIGNAL
        return None

    def exec_if_goto(self, ctx: TACParser.IfGotoContext):
        cond = self.eval_operand(ctx.operand())
        if cond:
            return ctx.ID().getText()
        return None

    def exec_assign(self, ctx: TACParser.AssignContext):
        target = ctx.ID().getText()
        self.set_var(target, self.eval_rhs(ctx.rhs()))

    def eval_rhs(self, ctx):
        if isinstance(ctx, TACParser.CallRhsContext):
            return self.call_function(ctx.ID().getText(), int(ctx.INT().getText()))
        if isinstance(ctx, TACParser.BinaryRhsContext):
            left = self.eval_operand(ctx.operand(0))
            right = self.eval_operand(ctx.operand(1))
            return self.apply_op(ctx.op().getText(), left, right)
        if isinstance(ctx, TACParser.NegRhsContext):
            return -self.eval_operand(ctx.operand())
        if isinstance(ctx, TACParser.NotRhsContext):
            return 0 if self.eval_operand(ctx.operand()) else 1
        if isinstance(ctx, TACParser.CopyRhsContext):
            return self.eval_operand(ctx.operand())

    def apply_op(self, op, left, right):
        table = {
            '+': lambda a, b: a + b, '-': lambda a, b: a - b,
            '*': lambda a, b: a * b, '/': lambda a, b: a // b,
            '>': lambda a, b: int(a > b), '>=': lambda a, b: int(a >= b),
            '<': lambda a, b: int(a < b), '<=': lambda a, b: int(a <= b),
            '==': lambda a, b: int(a == b), '!=': lambda a, b: int(a != b),
            '&&': lambda a, b: int(bool(a) and bool(b)),
            '||': lambda a, b: int(bool(a) or bool(b)),
        }
        return table[op](left, right)

    def exec_print(self, ctx: TACParser.PrintStatContext):
        parts = []
        for arg in ctx.printArg():
            if arg.STRING():
                parts.append(arg.STRING().getText()[1:-1])
            else:
                parts.append(str(self.eval_operand(arg.operand())))
        print(''.join(parts))

    def call_function(self, name, n_args):
        if name not in self.functions:
            raise RuntimeError(f"funcao '{name}' nao definida")
        func = self.functions[name]
        if len(self.pending_params) < n_args:
            raise RuntimeError(f"chamada a '{name}' espera {n_args} parametro(s), mas so ha {len(self.pending_params)} empilhado(s)")
        args = self.pending_params[-n_args:] if n_args > 0 else []
        self.pending_params = self.pending_params[:len(self.pending_params) - n_args]
        frame = {f'p{i}': args[i] for i in range(n_args)}
        self.call_stack.append(frame)
        saved_return = self.return_value
        self.return_value = 0
        self.run(func['body'], func['labels'])
        result = self.return_value
        self.return_value = saved_return
        self.call_stack.pop()
        return result