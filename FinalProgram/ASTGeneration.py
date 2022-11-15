from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Prog(ctx.getChild(0).accept(self))

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)
        else:
            return BinOp(ctx.getChild(1).getText(), ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.getChildCount() == 1:
            return ctx.getChild(0).accept(self)
        else:
            return BinOp(ctx.getChild(1).getText(), ctx.getChild(0).accept(self), ctx.getChild(2).accept(self))

    def visitFactor(self, ctx: BKITParser.FactorContext):
        return ctx.getChild(0).accept(self)

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        return Id(ctx.Identifier().getText())
