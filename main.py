import sys
import fileinput
from antlr4 import *
import argparse
from dist.strings68Lexer import strings68Lexer
from dist.strings68Parser import strings68Parser
from dist.strings68Visitor import strings68Visitor

vars = {}
loopend = 0


 
class MyVisitor(strings68Visitor):

    # Visit a parse tree produced by strings68Parser#program.
    def visitProgram(self, ctx:strings68Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#declaration.
    def visitDeclaration(self, ctx:strings68Parser.DeclarationContext):
        name = ctx.start.text
        vars[name] = ""
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#statement.
    def visitStatement(self, ctx:strings68Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by strings68Parser#ifstmt.
    def visitIfstmt(self, ctx:strings68Parser.IfstmtContext):
        r = ctx.getChild(4)
        l = ctx.getChild(2)
        rs=""
        ls=""

        if r != None and getattr(r, "start", None):
            rs = r.start.text
        if r != None and getattr(r, "symbol", None):
            rs = r.symbol.text
        if l != None and getattr(l, "start", None):
            ls = l.start.text
        if ls in vars:
            vall = vars[ls].strip('\"')
            valr = rs.strip('\"')
            if rs in vars:
                valr = vars[rs]
            if vall == valr:
                self.visitChildren(ctx)
        return self

    def visitLoopstmt(self, ctx:strings68Parser.LoopstmtContext):
        global loopend
        loopend = 0

        while (loopend==0):
            i = 0
            # Evaluate all statements inside the while loop.
            num = ctx.getChildCount()
            # stm = ctx.statement()
            while (i < num-1):
                st = ctx.getChild(i) 

                #op = getattr(st, "getSymbol", None)            
                #if op is not None:
                #    print("getSymbol() = " + str(st.getSymbol()))
                #op = getattr(st,"start", None)
                #if op is not None:
                #    print("start.text=" + st.start.text)
            
                self.visitChildren(st)
                i = i + 1            
        return self

    def visitBreakstmt(self, ctx:strings68Parser.BreakstmtContext):
        global loopend
        loopend = 1 
        return self
    
    # Visit a parse tree produced by strings68Parser#printstmt.
    def visitPrintstmt(self, ctx:strings68Parser.PrintstmtContext):
        s = ctx.getText()
        v = ctx.getChild(1).start.text
        if v in vars:
            print(vars[v])
        else:
            print(v)
        return self.visitChildren(ctx)

    # Visit a parse tree produced by strings68Parser#assignstmt.
    def visitAssignstmt(self, ctx:strings68Parser.AssignstmtContext):
        s = ctx.getText()
        i = s.find("=")
    #    name = ctx.NAME().symbol.text
        name = ctx.start.text.strip('\"')
        if ctx.getChildCount() > 4:
            val = ctx.getChild(3).start.text.strip('\"')
        else:   
            val = ctx.getChild(2).start.text.strip('\"')
        if name in vars and val in vars:
            updateval = vars[val]
            vars.update({name:updateval})
        else: 
            vars[name] = val
        return self.visitChildren(ctx)

    def visitToupperstmt(self, ctx:strings68Parser.ToupperstmtContext):
        s = ctx.getText()
        name = ctx.getChild(1).start.text
        if name in vars:
            vars[name]=vars[name].upper()
        return self.visitChildren(ctx)

    def visitTolowerstmt(self, ctx:strings68Parser.TolowerstmtContext):
        s = ctx.getText()
        name = ctx.getChild(1).start.text
        if name in vars:
            vars[name]=vars[name].lower()
        return self.visitChildren(ctx)

    def visitShiftlstmt(self, ctx:strings68Parser.ShiftlstmtContext):
        s = ctx.getText()
        v = ctx.getChild(1).start.text
        if v in vars:
            val = vars[v]
            valtemp = val[1:]
            val = valtemp 
            vars[v]=val
        return self.visitChildren(ctx)
    
    def visitShiftrstmt(self, ctx:strings68Parser.ShiftlstmtContext):
        s = ctx.getText()
        v = ctx.getChild(1).start.text
        if v in vars:
            val = vars[v]
            N = len(vars[v])
            valtemp = val[:N-1]
            val = valtemp
            vars[v]=val
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


    # Visit a parse tree produced by strings68Parser#integer.
    def visitString(self, ctx:strings68Parser.StringContext):
        return self.visitChildren(ctx)


if __name__ == "__main__":
   
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', type=str,required=True) 
    args = parser.parse_args()
   
    # data =  InputStream(input(">>> "))
    # lexer
    lexer = strings68Lexer(FileStream(args.f))
    stream = CommonTokenStream(lexer)
    # parser
    parser = strings68Parser(stream)
   
    tree = parser.program()
    #handleExpression(tree)
    # evaluator
    visitor = MyVisitor()
    output = visitor.visitProgram(tree)

