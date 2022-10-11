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

program: statementList EOF;

statementList: statement*;

statement: expressionList Semi;

Semi: ';';

expressionList: expression*;

expression: metaType IdLiteral '=' term | term;

metaType: IntegerType | FloatType;

term: FloatLiteral | IntegerLiteral | IdLiteral;

IntegerType: 'int';
FloatType: 'float';

FloatLiteral:
	FloatIntLiteral FloatDecLiteral
	| (FloatIntLiteral | FloatDecLiteral) FloatExpLiteral
	| FloatIntLiteral FloatDecLiteral FloatExpLiteral;
fragment FloatIntLiteral: Sign? IntegerLiteral+;
fragment FloatDecLiteral: '.' IntegerLiteral+;
fragment FloatExpLiteral: [Ee] Sign? IntegerLiteral+;
Sign: [+-];
IntegerLiteral: [0-9]+;
IdLiteral: [a-z]+;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
