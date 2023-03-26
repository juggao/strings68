# Generated from strings.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,59,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,3,3,31,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,40,8,4,1,5,4,5,43,8,
        5,11,5,12,5,44,1,6,4,6,48,8,6,11,6,12,6,49,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,1,0,2,3,0,48,
        57,65,90,97,122,2,0,9,9,32,32,62,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,
        0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,30,1,0,0,0,9,39,1,0,0,
        0,11,42,1,0,0,0,13,47,1,0,0,0,15,53,1,0,0,0,17,18,5,61,0,0,18,2,
        1,0,0,0,19,20,5,40,0,0,20,4,1,0,0,0,21,22,5,41,0,0,22,6,1,0,0,0,
        23,24,5,104,0,0,24,25,5,101,0,0,25,26,5,108,0,0,26,27,5,108,0,0,
        27,31,5,111,0,0,28,29,5,104,0,0,29,31,5,105,0,0,30,23,1,0,0,0,30,
        28,1,0,0,0,31,8,1,0,0,0,32,33,5,98,0,0,33,34,5,121,0,0,34,40,5,101,
        0,0,35,36,5,116,0,0,36,37,5,97,0,0,37,38,5,116,0,0,38,40,5,97,0,
        0,39,32,1,0,0,0,39,35,1,0,0,0,40,10,1,0,0,0,41,43,7,0,0,0,42,41,
        1,0,0,0,43,44,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,12,1,0,0,0,
        46,48,7,1,0,0,47,46,1,0,0,0,48,49,1,0,0,0,49,47,1,0,0,0,49,50,1,
        0,0,0,50,51,1,0,0,0,51,52,6,6,0,0,52,14,1,0,0,0,53,54,5,112,0,0,
        54,55,5,114,0,0,55,56,5,105,0,0,56,57,5,110,0,0,57,58,5,116,0,0,
        58,16,1,0,0,0,5,0,30,39,44,49,1,6,0,0
    ]

class stringsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    HELLO = 4
    BYE = 5
    STRING = 6
    WS = 7
    PRINT = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "HELLO", "BYE", "STRING", "WS", "PRINT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "HELLO", "BYE", "STRING", "WS", 
                  "PRINT" ]

    grammarFileName = "strings.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


