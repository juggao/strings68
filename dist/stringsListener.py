# Generated from strings.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stringsParser import stringsParser
else:
    from stringsParser import stringsParser

# This class defines a complete listener for a parse tree produced by stringsParser.
class stringsListener(ParseTreeListener):

    # Enter a parse tree produced by stringsParser#StringExpr.
    def enterStringExpr(self, ctx:stringsParser.StringExprContext):
        pass

    # Exit a parse tree produced by stringsParser#StringExpr.
    def exitStringExpr(self, ctx:stringsParser.StringExprContext):
        pass


    # Enter a parse tree produced by stringsParser#ByeExpr.
    def enterByeExpr(self, ctx:stringsParser.ByeExprContext):
        pass

    # Exit a parse tree produced by stringsParser#ByeExpr.
    def exitByeExpr(self, ctx:stringsParser.ByeExprContext):
        pass


    # Enter a parse tree produced by stringsParser#HelloExpr.
    def enterHelloExpr(self, ctx:stringsParser.HelloExprContext):
        pass

    # Exit a parse tree produced by stringsParser#HelloExpr.
    def exitHelloExpr(self, ctx:stringsParser.HelloExprContext):
        pass


    # Enter a parse tree produced by stringsParser#ParenExpr.
    def enterParenExpr(self, ctx:stringsParser.ParenExprContext):
        pass

    # Exit a parse tree produced by stringsParser#ParenExpr.
    def exitParenExpr(self, ctx:stringsParser.ParenExprContext):
        pass


    # Enter a parse tree produced by stringsParser#InfixExpr.
    def enterInfixExpr(self, ctx:stringsParser.InfixExprContext):
        pass

    # Exit a parse tree produced by stringsParser#InfixExpr.
    def exitInfixExpr(self, ctx:stringsParser.InfixExprContext):
        pass


    # Enter a parse tree produced by stringsParser#PrintExpr.
    def enterPrintExpr(self, ctx:stringsParser.PrintExprContext):
        pass

    # Exit a parse tree produced by stringsParser#PrintExpr.
    def exitPrintExpr(self, ctx:stringsParser.PrintExprContext):
        pass



del stringsParser