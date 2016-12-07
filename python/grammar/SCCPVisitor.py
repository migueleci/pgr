# Generated from python/grammar/SCCP.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SCCPParser import SCCPParser
else:
    from SCCPParser import SCCPParser

# This class defines a complete generic visitor for a parse tree produced by SCCPParser.

class SCCPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SCCPParser#sys.
    def visitSys(self, ctx:SCCPParser.SysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#decl.
    def visitDecl(self, ctx:SCCPParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#vint.
    def visitVint(self, ctx:SCCPParser.VintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#vbool.
    def visitVbool(self, ctx:SCCPParser.VboolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#body.
    def visitBody(self, ctx:SCCPParser.BodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#line.
    def visitLine(self, ctx:SCCPParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#parallel.
    def visitParallel(self, ctx:SCCPParser.ParallelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#tell.
    def visitTell(self, ctx:SCCPParser.TellContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#procloc.
    def visitProcloc(self, ctx:SCCPParser.ProclocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#ask.
    def visitAsk(self, ctx:SCCPParser.AskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#bool.
    def visitBool(self, ctx:SCCPParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#and.
    def visitAnd(self, ctx:SCCPParser.AndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#cexpr.
    def visitCexpr(self, ctx:SCCPParser.CexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#id.
    def visitId(self, ctx:SCCPParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#loc.
    def visitLoc(self, ctx:SCCPParser.LocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#expr.
    def visitExpr(self, ctx:SCCPParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#op.
    def visitOp(self, ctx:SCCPParser.OpContext):
        return self.visitChildren(ctx)



del SCCPParser