from ASTUtils import *
from functools import reduce


class CodeRunner:
    def visitInteger(self, ctx: Int):
        return ctx.value

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
        elif ctx.op == "%":
            return left % right

    def visitProgram(self, ctx: Prog):
        return str(ctx.expr.accept(self))
