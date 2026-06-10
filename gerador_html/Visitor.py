from HtmlVisitor import HtmlVisitor


class HtmlOutput():
    """Acumula o HTML gerado e imprime ao fechar."""

    def __init__(self):
        # Inicializa o documento HTML com cabeçalho e abertura do form
        self.conteudo  = "<html>\n"
        self.conteudo += "<head><title>Formulario</title></head>\n"
        self.conteudo += "<body>\n"
        self.conteudo += "<form>\n"
        self.count = 0

    def addText(self, cols, rows, texto):
        # Textarea com rótulo, dimensões e nome sequencial
        self.conteudo += texto + "<br>\n"
        self.conteudo += (
            f"<textarea name='Q{self.count}' "
            f"cols='{cols}' rows='{rows}'></textarea><br>\n"
        )
        self.conteudo += "<br>\n\n"
        self.count += 1

    def addRadio(self, texto, opcoes):
        # Radio buttons com mesmo name para garantir seleção única
        self.conteudo += texto + "<br>\n"
        for val in opcoes:
            self.conteudo += (
                f"<input type='radio' name='Q{self.count}' "
                f"value='{val}'>{val}<br>\n"
            )
        self.conteudo += "<br>\n\n"
        self.count += 1

    def addCheckBox(self, texto, opcoes):
        # Cada checkbox recebe name sequencial independente
        self.conteudo += texto + "<br>\n"
        for val in opcoes:
            self.conteudo += (
                f"<input type='checkbox' name='Q{self.count}' "
                f"value='{val}'>{val}<br>\n"
            )
            self.count += 1
        self.conteudo += "<br>\n\n"

    def addMenu(self, id_, label, opcoes):
        # Select com label associado via atributo 'for'
        self.conteudo += f"<label for='{id_}'>{label}</label><br>\n"
        self.conteudo += f"<select name='{id_}' id='{id_}'>\n"
        for valor, rotulo in opcoes:
            self.conteudo += f"  <option value='{valor}'>{rotulo}</option>\n"
        self.conteudo += "</select><br>\n"
        self.conteudo += "<br>\n\n"
        self.count += 1

    def addBotao(self, rotulo, alerta):
        # Botão com onclick disparando alert com a mensagem fornecida
        self.conteudo += (
            f"<button type='button' onclick=\"alert('{alerta}')\">"
            f"{rotulo}</button><br>\n"
        )
        self.conteudo += "<br>\n\n"
        self.count += 1

    def addTabela(self, caption, cabecalho, linhas):
        # Tabela com legenda, linha de cabeçalho <th> e linhas de dados <td>
        self.conteudo += "<table border='1'>\n"
        self.conteudo += f"  <caption>{caption}</caption>\n"
        self.conteudo += "  <tr>\n"
        for col in cabecalho:
            self.conteudo += f"    <th>{col}</th>\n"
        self.conteudo += "  </tr>\n"
        for linha in linhas:
            self.conteudo += "  <tr>\n"
            for cel in linha:
                self.conteudo += f"    <td>{cel}</td>\n"
            self.conteudo += "  </tr>\n"
        self.conteudo += "</table><br>\n"
        self.conteudo += "<br>\n\n"
        self.count += 1

    def close(self):
        # Fecha as tags do documento e imprime o HTML completo
        self.conteudo += "</form>\n"
        self.conteudo += "</body>\n"
        self.conteudo += "</html>\n"
        print(self.conteudo)


class Visitor(HtmlVisitor):
    """Percorre a árvore sintática e aciona HtmlOutput para cada nó."""

    def __init__(self):
        self.html = HtmlOutput()

    def visitRoot(self, ctx):
        # Visita cada questão da raiz e fecha o documento ao final
        for questao in ctx.getChildren():
            self.visit(questao)
        self.html.close()

    def visitQuestao(self, ctx):
        # Delega para o tipo concreto de questão
        filhos = list(ctx.getChildren())
        return self.visit(filhos[0])

    def visitQTexto(self, ctx):
        # Extrai cols, rows e texto; gera textarea
        filhos = list(ctx.getChildren())
        if len(filhos) == 4:
            cols  = filhos[1].getText()
            rows  = filhos[2].getText()
            texto = self.visit(filhos[3])
            self.html.addText(cols, rows, texto)

    def visitQRadioBox(self, ctx):
        # Extrai pergunta e opções; gera radio buttons
        filhos = list(ctx.getChildren())
        if len(filhos) == 3:
            texto  = self.visit(filhos[1])
            opcoes = self.visit(filhos[2])
            self.html.addRadio(texto, opcoes)

    def visitQCheckBox(self, ctx):
        # Extrai pergunta e opções; gera checkboxes
        filhos = list(ctx.getChildren())
        if len(filhos) == 3:
            texto  = self.visit(filhos[1])
            opcoes = self.visit(filhos[2])
            self.html.addCheckBox(texto, opcoes)

    def visitQMenu(self, ctx):
        # Extrai id, label e opções; gera select dropdown
        filhos = list(ctx.getChildren())
        if len(filhos) == 4:
            id_    = self.visit(filhos[1])
            label  = self.visit(filhos[2])
            opcoes = self.visit(filhos[3])
            self.html.addMenu(id_, label, opcoes)

    def visitQBotao(self, ctx):
        # Extrai rótulo e mensagem do alerta; gera button
        filhos = list(ctx.getChildren())
        if len(filhos) == 3:
            rotulo = self.visit(filhos[1])
            alerta = self.visit(filhos[2])
            self.html.addBotao(rotulo, alerta)

    def visitQTabela(self, ctx):
        # Extrai caption, cabeçalho e linhas; gera table
        filhos = list(ctx.getChildren())
        if len(filhos) == 4:
            caption   = self.visit(filhos[1])
            cabecalho = self.visit(filhos[2])
            linhas    = self.visit(filhos[3])
            self.html.addTabela(caption, cabecalho, linhas)

    def visitOpcoes(self, ctx):
        # Conta strings desconsiderando '(' ')' e ',' e retorna lista
        filhos = list(ctx.getChildren())
        qtd    = (len(filhos) - 2) // 2  # desconta '(' ')' e vírgulas
        opcoes = []
        for i in range(qtd + 1):
            opcoes.append(self.visit(ctx.str_(i)))
        return opcoes

    def visitMenuOpcoes(self, ctx):
        # Retorna lista de tuplas (valor, rotulo) para o select
        return [self.visit(opcao) for opcao in ctx.menuOpcao()]

    def visitMenuOpcao(self, ctx):
        # Par str_ ':' str_ → retorna (valor, rotulo)
        filhos = list(ctx.getChildren())
        valor  = self.visit(filhos[0])
        rotulo = self.visit(filhos[2])
        return (valor, rotulo)

    def visitLinhaCabecalho(self, ctx):
        # Retorna lista de strings para os <th> da tabela
        return [self.visit(s) for s in ctx.str_()]

    def visitLinhaDados(self, ctx):
        # Retorna lista de listas, cada uma representando uma linha <tr>
        return [self.visit(linha) for linha in ctx.linha()]

    def visitLinha(self, ctx):
        # Retorna lista de strings para os <td> de uma linha
        return [self.visit(s) for s in ctx.str_()]

    def visitStr_(self, ctx):
        # Remove as aspas duplas do token STRING e retorna o valor puro
        filhos = list(ctx.getChildren())
        return filhos[0].getText().replace('"', '')