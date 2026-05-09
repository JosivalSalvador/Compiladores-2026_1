import sys
from antlr4 import CommonTokenStream, FileStream, TerminalNode
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser

# Regras que sempre expandem em múltiplas linhas (estrutura de alto nível do programa)
# Tudo abaixo disso fica inline ou recebe tratamento especial
EXPAND = {'program', 'definition', 'function_definition', 'function_body', 'block'}


def inline(node, rule_names):
    # Token terminal: retorna o texto diretamente (ex: 'int', '+', '42')
    if isinstance(node, TerminalNode):
        return node.getText()
    # Nó interno: serializa recursivamente como (regra filho1 filho2 ...)
    rule = rule_names[node.getRuleIndex()]
    children = ' '.join(inline(node.getChild(i), rule_names) for i in range(node.getChildCount()))
    return f'({rule} {children})'


def has_complex_child(node, rule_names):
    # Detecta se o statement contém if/while/block como filho direto
    # Esses casos precisam de expansão em múltiplas linhas
    for i in range(node.getChildCount()):
        child = node.getChild(i)
        if not isinstance(child, TerminalNode):
            if rule_names[child.getRuleIndex()] in ('statement', 'block'):
                return True
    return False


def print_statement(node, rule_names, indent):
    # Imprime statement com if/while/block de forma legível:
    # tokens terminais consecutivos (ex: 'if ( <expr> )') ficam numa linha só,
    # filhos statement/block são expandidos recursivamente abaixo
    pad  = '  ' * indent
    pad1 = '  ' * (indent + 1)
    print(f'{pad}(statement')

    pending_tokens = []  # acumula tokens terminais e expressões inline

    def flush_tokens():
        # Imprime os tokens acumulados numa linha e limpa o buffer
        if pending_tokens:
            print(f'{pad1}{" ".join(pending_tokens)}')
            pending_tokens.clear()

    for i in range(node.getChildCount()):
        child = node.getChild(i)
        if isinstance(child, TerminalNode):
            # Terminal (if, while, else, (, ), ;) → acumula para imprimir junto
            pending_tokens.append(child.getText())
        else:
            rule = rule_names[child.getRuleIndex()]
            if rule in ('statement', 'block'):
                # Filho complexo: despeja tokens acumulados e expande o filho
                flush_tokens()
                print_tree(child, rule_names, indent + 1)
            else:
                # expression e similares: serializa inline junto com os tokens pendentes
                pending_tokens.append(inline(child, rule_names))

    flush_tokens()
    print(f'{pad})')


def print_tree(node, rule_names, indent=0):
    pad = '  ' * indent

    if isinstance(node, TerminalNode):
        # Token folha: imprime com indentação
        print(f'{pad}{node.getText()}')
        return

    rule = rule_names[node.getRuleIndex()]

    if rule in EXPAND:
        # Regras de alto nível: cada filho em sua própria linha indentada
        print(f'{pad}({rule}')
        for i in range(node.getChildCount()):
            print_tree(node.getChild(i), rule_names, indent + 1)
        print(f'{pad})')
        return

    if rule == 'statement' and has_complex_child(node, rule_names):
        # Statement com if/while/block: tratamento especial para manter legibilidade
        print_statement(node, rule_names, indent)
        return

    # Qualquer outro nó (expression, binary, unary, primary, etc.): tudo inline
    print(f'{pad}{inline(node, rule_names)}')


def main():
    # Lê o arquivo fonte passado como argumento de linha de comando
    input_stream = FileStream(sys.argv[1], encoding='utf-8')
    # Instancia o analisador léxico (lexer)
    lexer = MiniCLexer(input_stream)
    # Instancia o fluxo de tokens
    stream = CommonTokenStream(lexer)
    # Instancia o analisador sintático (parser)
    parser = MiniCParser(stream)
    # Executa a análise sintática a partir da regra inicial (program)
    tree = parser.program()
    # Imprime a árvore de análise sintática (parse tree)
    print_tree(tree, parser.ruleNames)


if __name__ == '__main__':
    main()