from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        id = ctx.getChild(0).accept(self)
        return Prog(id)

    def visitIntTerm(self, ctx: BKITParser.IntTermContext):
        if ctx.Sub():
            return Int(-int(ctx.Integer().getText()))
        return Int(int(ctx.Integer().getText()))

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        return Id(ctx.Identifier().getText())
