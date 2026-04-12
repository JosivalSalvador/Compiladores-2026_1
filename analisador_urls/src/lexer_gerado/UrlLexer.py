# Generated from /home/gaby/Documentos/Compiladores-2026_1/analisador_urls/gramatica/UrlLexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,2,26,6,-1,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,
        0,1,0,1,0,1,0,3,0,18,8,0,1,1,4,1,21,8,1,11,1,12,1,22,1,1,1,1,0,0,
        2,1,1,3,2,1,0,1,3,0,9,10,13,13,32,32,28,0,1,1,0,0,0,0,3,1,0,0,0,
        1,17,1,0,0,0,3,20,1,0,0,0,5,6,5,104,0,0,6,7,5,116,0,0,7,8,5,116,
        0,0,8,18,5,112,0,0,9,10,5,104,0,0,10,11,5,116,0,0,11,12,5,116,0,
        0,12,13,5,112,0,0,13,18,5,115,0,0,14,15,5,102,0,0,15,16,5,116,0,
        0,16,18,5,112,0,0,17,5,1,0,0,0,17,9,1,0,0,0,17,14,1,0,0,0,18,2,1,
        0,0,0,19,21,7,0,0,0,20,19,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,
        23,1,0,0,0,23,24,1,0,0,0,24,25,6,1,0,0,25,4,1,0,0,0,3,0,17,22,1,
        6,0,0
    ]

class UrlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PROTOCOL = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "PROTOCOL", "WS" ]

    ruleNames = [ "PROTOCOL", "WS" ]

    grammarFileName = "UrlLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


