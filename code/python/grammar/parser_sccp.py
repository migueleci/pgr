__author__ = 'mromero'

import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from SCCPLexer import SCCPLexer
from SCCPParser import SCCPParser
# from RewriterListener import RewriterListener
from RewriterVisitor import RewriterVisitor

if __name__ == '__main__':
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = SCCPLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SCCPParser(token_stream)
    tree = parser.sys()

    # lisp_tree_str = tree.toStringTree(recog=parser)
    # print(lisp_tree_str)

    # walker = ParseTreeWalker()
    # walker.walk(RewriterListener(), tree)
    # print()

    visitor = RewriterVisitor()
    visitor.visit(tree)