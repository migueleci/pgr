# Generated from python/grammar/SCCP.g4 by ANTLR 4.5.3
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by SCCPParser.

class SCCPVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SCCPParser#sys.
    def visitSys(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#decl.
    def visitDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#vint.
    def visitVint(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#vbool.
    def visitVbool(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#body.
    def visitBody(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#line.
    def visitLine(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#parallel.
    def visitParallel(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#tell.
    def visitTell(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#procloc.
    def visitProcloc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#ask.
    def visitAsk(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#bool.
    def visitBool(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#and.
    def visitAnd(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#cexpr.
    def visitCexpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#id.
    def visitId(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#loc.
    def visitLoc(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SCCPParser#op.
    def visitOp(self, ctx):
        return self.visitChildren(ctx)


