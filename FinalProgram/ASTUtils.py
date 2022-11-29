from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass


def printlist(lst, f=str, start="[", sepa=",", end="]"):
    return start + sepa.join(f(i) for i in lst) + end


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    @abstractmethod
    def accept(self, v, param):
        pass


class Exp(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Int(Exp):
    value: int

    def __str__(self):
        return "INT(%d)" % self.value

    def accept(self, v):
        return v.visitInteger(self)


@dataclass
class BinOp(Exp):
    op: str
    left: Exp
    right: Exp

    def __str__(self):
        return 'BinOp("' + self.op + '",' + str(self.left
                                               ) + "," + str(self.right) + ")"

    def accept(self, v):
        return v.visitBinaryOp(self)


@dataclass
class Prog(AST):
    expr: Exp

    def __str__(self):
        return "Prog(" + str(self.expr) + ")"

    def accept(self, v):
        return v.visitProgram(self)
