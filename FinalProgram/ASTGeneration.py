from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        id = ctx.idTerm().accept(self)
        return Prog(id)

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())
