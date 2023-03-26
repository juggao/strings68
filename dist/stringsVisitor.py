# Generated from strings.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .stringsParser import stringsParser
else:
    from stringsParser import stringsParser

# This class defines a complete generic visitor for a parse tree produced by stringsParser.

class stringsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by stringsParser#StringExpr.
    def visitStringExpr(self, ctx:stringsParser.StringExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stringsParser#ByeExpr.
    def visitByeExpr(self, ctx:stringsParser.ByeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stringsParser#HelloExpr.
    def visitHelloExpr(self, ctx:stringsParser.HelloExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stringsParser#ParenExpr.
    def visitParenExpr(self, ctx:stringsParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stringsParser#InfixExpr.
    def visitInfixExpr(self, ctx:stringsParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by stringsParser#PrintExpr.
    def visitPrintExpr(self, ctx:stringsParser.PrintExprContext):
        return self.visitChildren(ctx)



del stringsParser