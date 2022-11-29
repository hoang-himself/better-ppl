from ASTUtils import *
from functools import reduce


class CodeRunner:
    def visitProgram(self, ctx: Prog):
        return str(ctx.expr.accept(self))

    def visitInteger(self, ctx: Int):
        return ctx.value

    def visitUnaryOp(self, ctx: UnaryOp):
        body = ctx.body.accept(self)
        if ctx.op == "-":
            return -body

    def visitBinaryOp(self, ctx: BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)
        if ctx.op == "+":
            return left + right
        elif ctx.op == "-":
            return left - right
        elif ctx.op == "*":
            return left * right
        elif ctx.op == "/":
            return left / right
