from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple


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
class UnaryOp(Exp):
    op: str
    body: Exp

    def __str__(self):
        return 'UnaryOp("' + self.op + '",' + str(self.body) + ")"


@dataclass
class Prog(AST):
    expr: Exp

    def __str__(self):
        return "Prog(" + str(self.expr) + ")"
