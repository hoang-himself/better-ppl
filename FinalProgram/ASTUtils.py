from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple


def printlist(lst, f=str, start="[", sepa=",", end="]"):
    return start + sepa.join(f(i) for i in lst) + end


class AST(ABC):
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Exp(AST):
    __metaclass__ = ABCMeta
    pass


@dataclass
class Id(Exp):
    name: str

    def __str__(self):
        return "ID(" + self.name + ")"


@dataclass
class Int(Exp):
    value: int

    def __str__(self):
        return "INT(%d)" % self.value


@dataclass
class BinOp(Exp):
    op: str
    left: Exp
    right: Exp

    def __str__(self):
        return "BinOp(\"" + self.op + "\"," + str(self.left) + "," + str(
            self.right
        ) + ")"


@dataclass
class Prog(AST):
    expr: List[Exp]

    def __str__(self):
        return "Prog(" + printlist(self.expr, start="", end="") + ")"
