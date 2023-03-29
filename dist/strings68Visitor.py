# Generated from strings68.g4 by ANTLR 4.12.0
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .strings68Parser import strings68Parser
else:
    from strings68Parser import strings68Parser

# This class defines a complete generic visitor for a parse tree produced by strings68Parser.

class strings68Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by strings68Parser#program.
    def visitProgram(self, ctx:strings68Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#declaration.
    def visitDeclaration(self, ctx:strings68Parser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#statement.
    def visitStatement(self, ctx:strings68Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#ifstmt.
    def visitIfstmt(self, ctx:strings68Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#loopstmt.
    def visitLoopstmt(self, ctx:strings68Parser.LoopstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#breakstmt.
    def visitBreakstmt(self, ctx:strings68Parser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#printstmt.
    def visitPrintstmt(self, ctx:strings68Parser.PrintstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#toupperstmt.
    def visitToupperstmt(self, ctx:strings68Parser.ToupperstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#tolowerstmt.
    def visitTolowerstmt(self, ctx:strings68Parser.TolowerstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#shiftlstmt.
    def visitShiftlstmt(self, ctx:strings68Parser.ShiftlstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#shiftrstmt.
    def visitShiftrstmt(self, ctx:strings68Parser.ShiftrstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#maskstmt.
    def visitMaskstmt(self, ctx:strings68Parser.MaskstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#assignstmt.
    def visitAssignstmt(self, ctx:strings68Parser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#expression.
    def visitExpression(self, ctx:strings68Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#term.
    def visitTerm(self, ctx:strings68Parser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#identifier.
    def visitIdentifier(self, ctx:strings68Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#stringchars.
    def visitStringchars(self, ctx:strings68Parser.StringcharsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#string.
    def visitString(self, ctx:strings68Parser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#bool.
    def visitBool(self, ctx:strings68Parser.BoolContext):
        return self.visitChildren(ctx)



del strings68Parser