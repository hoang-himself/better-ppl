from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *
from functools import reduce


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Prog(self.visit(ctx.getChild(0)))

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinOp(
                ctx.getChild(1).getText(), self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2))
            )

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return BinOp(
                ctx.getChild(1).getText(), self.visit(ctx.getChild(0)),
                self.visit(ctx.getChild(2))
            )

    def visitFactor(self, ctx: BKITParser.FactorContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        else:
            return UnaryOp(
                ctx.getChild(0).getText(), self.visit(ctx.getChild(1))
            )

    def visitIntTerm(self, ctx: BKITParser.IntTermContext):
        return Int(int(ctx.getChild(0).getText()))
