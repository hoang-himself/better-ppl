from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils

            We need to visit all children of program. They are list of expressions.
            ctx.expression() returns the list we desire.

            Then we call expression.accept(self) or self.visitExpression(expression),
            function visitExpression() will be triggered.
        '''
        return Prog(ctx.expressions().accept(self))

    def visitExpressions(self, ctx: BKITParser.ExpressionsContext):
        list_expressions = []
        if ctx.expressions():
            list_expressions.extend(ctx.expressions().accept(self))
            list_expressions.append(ctx.expression().accept(self))

        return list_expressions

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        '''
            BinOp: dataclass in ASTUtils
        '''
        if ctx.expression():
            sign = ""
            if ctx.Add():
                sign = ctx.Add().getText()
            elif ctx.Sub():
                sign = ctx.Sub().getText()

            return BinOp(
                sign,
                ctx.expression().accept(self),
                ctx.factor().accept(self)
            )
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx: BKITParser.FactorContext):
        '''
            BinOp: dataclass in ASTUtils
        '''
        if ctx.factor():
            sign = ""
            if ctx.Mul():
                sign = ctx.Mul().getText()
            elif ctx.Div():
                sign = ctx.Div().getText()

            return BinOp(
                sign,
                ctx.factor().accept(self),
                ctx.term().accept(self)
            )
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: BKITParser.TermContext):
        '''
            As defined in BKIT.g4, term can be either an intTerm or an idTerm,
            so that we need to check if this term contains intTerm or idTerm.
        '''
        if ctx.idTerm():
            return ctx.idTerm().accept(self)
        elif ctx.intTerm():
            return ctx.intTerm().accept(self)

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
