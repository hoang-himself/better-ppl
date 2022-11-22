from ASTUtils import *
from functools import reduce


class CodeRunner:
    def visitProgram(self, ctx: Prog):
        return "\n".join([str(expr.accept(self)) for expr in ctx.expr])

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

    def visitInteger(self, ctx: Int):
        return ctx.value
