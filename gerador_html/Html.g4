grammar Html;

// Regra raiz: uma ou mais questões
root: questao+;

// Tipos de questão suportados
questao: (qTexto | qRadioBox | qCheckBox | qMenu | qBotao | qTabela);

// Área de texto livre com dimensões cols x rows
qTexto:    'TEXTO'         NUMERO NUMERO str_;

// Seleção de uma opção via radio button
qRadioBox: 'ESCOLHAUMA'    str_ opcoes;

// Seleção de múltiplas opções via checkbox
qCheckBox: 'ESCOLHAVARIAS' str_ opcoes;

// Menu de seleção (dropdown): id do select, label, opções valor:rotulo
qMenu:     'MENU'          str_ str_ menuOpcoes;

// Botão com alerta: rótulo do botão e mensagem do alert
qBotao:    'BOTAO'         str_ str_;

// Tabela: legenda, linha de cabeçalho, linhas de dados
qTabela:   'TABELA'        str_ linhaCabecalho linhaDados;

// Lista de opções para radio/checkbox
opcoes:         '(' str_ (',' str_)* ')';

// Lista de opções para o menu dropdown
menuOpcoes:     '(' menuOpcao (',' menuOpcao)* ')';

// Par valor:rotulo de uma opção do menu
menuOpcao:      str_ ':' str_;

// Cabeçalho da tabela: uma ou mais colunas
linhaCabecalho: '(' str_ (',' str_)* ')';

// Conjunto de linhas de dados da tabela
linhaDados:     '(' linha (',' linha)* ')';

// Uma linha da tabela com uma ou mais células
linha:          '(' str_ (',' str_)* ')';

str_: STRING;

// TOKENS
NUMERO:  [0-9]+;
STRING:  '"' (~["])* '"';
IGNORE:  [ \n\r\t] -> skip;
COMMENT: '#' ~[\r\n]* -> skip;