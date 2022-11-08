from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        if ctx.Add() or ctx.Sub():
            op = ctx.getChild(1).getText()
            lhs = self.visit(ctx.getChild(0))
            rhs = self.visit(ctx.getChild(2))
            return Prog(BinOp(op, lhs, rhs))
        else:
            return Prog(self.visit(ctx.getChild(0)))

    def visitTerm(self, ctx: BKITParser.TermContext):
        return self.visit(ctx.getChild(0))

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
