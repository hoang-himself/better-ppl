grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

program: stmtList EOF;

stmtList: stmt*;

stmt: exprList Semi;

Semi: ';';

exprList: expr*;

expr: metaDecl | term;

metaDecl: metaType declList;

declList: decl (',' decl)* |;

decl: IdLit '=' term;

metaType: FloatType | IntType;

term: FloatLit | IntLit | IdLit;

IntType: 'int';
FloatType: 'float';

FloatLit:
	FloatIntLit FloatDecLit
	| (FloatIntLit | FloatDecLit) FloatExpLit
	| FloatIntLit FloatDecLit FloatExpLit;
fragment FloatIntLit: Sign? IntLit+;
fragment FloatDecLit: '.' IntLit+;
fragment FloatExpLit: [Ee] Sign? IntLit+;
Sign: [+-];
IntLit: [0-9]+;
IdLit: [a-z]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
