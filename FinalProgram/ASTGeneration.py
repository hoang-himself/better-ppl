from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        if ctx.idTerm():
            return Prog(ctx.idTerm().accept(self))
        elif ctx.intTerm():
            return Prog(ctx.intTerm().accept(self))

    def visitIntTerm(self, ctx: BKITParser.IntTermContext):
        '''
            Int: dataclass in ASTUtils
        '''
        return Int(int(ctx.Integer().getText()))

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())
