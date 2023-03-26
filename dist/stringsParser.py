# Generated from strings.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,8,23,2,0,7,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,0,1,0,1,0,0,0,26,
        0,12,1,0,0,0,2,3,6,0,-1,0,3,13,5,6,0,0,4,5,5,2,0,0,5,6,3,0,0,0,6,
        7,5,3,0,0,7,13,1,0,0,0,8,13,5,4,0,0,9,13,5,5,0,0,10,11,5,8,0,0,11,
        13,5,6,0,0,12,2,1,0,0,0,12,4,1,0,0,0,12,8,1,0,0,0,12,9,1,0,0,0,12,
        10,1,0,0,0,13,19,1,0,0,0,14,15,10,6,0,0,15,16,5,1,0,0,16,18,3,0,
        0,7,17,14,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,1,
        1,0,0,0,21,19,1,0,0,0,2,12,19
    ]

class stringsParser ( Parser ):

    grammarFileName = "strings.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "HELLO", "BYE", "STRING", "WS", "PRINT" ]

    RULE_expr = 0

    ruleNames =  [ "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    HELLO=4
    BYE=5
    STRING=6
    WS=7
    PRINT=8

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return stringsParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(stringsParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class ByeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def BYE(self):
            return self.getToken(stringsParser.BYE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterByeExpr" ):
                listener.enterByeExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitByeExpr" ):
                listener.exitByeExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitByeExpr" ):
                return visitor.visitByeExpr(self)
            else:
                return visitor.visitChildren(self)


    class HelloExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def HELLO(self):
            return self.getToken(stringsParser.HELLO, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHelloExpr" ):
                listener.enterHelloExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHelloExpr" ):
                listener.exitHelloExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelloExpr" ):
                return visitor.visitHelloExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(stringsParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(stringsParser.ExprContext)
            else:
                return self.getTypedRuleContext(stringsParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)


    class PrintExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a stringsParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(stringsParser.STRING, 0)
        def PRINT(self):
            return self.getToken(stringsParser.PRINT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintExpr" ):
                return visitor.visitPrintExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = stringsParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = stringsParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 3
                localctx.atom = self.match(stringsParser.STRING)
                pass
            elif token in [2]:
                localctx = stringsParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 4
                self.match(stringsParser.T__1)
                self.state = 5
                self.expr(0)
                self.state = 6
                self.match(stringsParser.T__2)
                pass
            elif token in [4]:
                localctx = stringsParser.HelloExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                localctx.atom = self.match(stringsParser.HELLO)
                pass
            elif token in [5]:
                localctx = stringsParser.ByeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 9
                localctx.atom = self.match(stringsParser.BYE)
                pass
            elif token in [8]:
                localctx = stringsParser.PrintExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 10
                localctx.atom = self.match(stringsParser.PRINT)
                self.state = 11
                self.match(stringsParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 19
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = stringsParser.InfixExprContext(self, stringsParser.ExprContext(self, _parentctx, _parentState))
                    localctx.left = _prevctx
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 14
                    if not self.precpred(self._ctx, 6):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                    self.state = 15
                    self.match(stringsParser.T__0)
                    self.state = 16
                    localctx.right = self.expr(7) 
                self.state = 21
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[0] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         




