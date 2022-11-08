from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        op = ctx.getChild(1).getText()
        lhs = self.visit(ctx.idTerm(0))
        rhs = self.visit(ctx.idTerm(1))
        return BinOp(op, lhs, rhs)

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())
