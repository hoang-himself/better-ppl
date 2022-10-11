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

program: varDeclStmt EOF;

varDeclStmt: typeInd Id Assignment primaryLiteral Semi;

typeInd: Int | Flt;

primaryLiteral: integerLiteral | floatLiteral;

integerLiteral: Integer;
floatLiteral: Float;

Int: 'int';
Flt: 'float';
Semi: ';';
Assignment: '=';

Id: NonDigit ( NonDigit | Digit)*;

Integer: Sign? ( NonZeroDigit Digit* | '0');

Float:
	Sign? (
		FragtionalConstant ExponentPart? FloatingPart?
		| DigitSequence ExponentPart FloatingPart?
	);

fragment FragtionalConstant:
	DigitSequence '.' DigitSequence
	| DigitSequence '.';

fragment ExponentPart: [eE] Sign? DigitSequence;

fragment FloatingPart: 'f' | 'F';

fragment Sign: '+' | '-';

fragment DigitSequence: Digit+;

fragment NonDigit: [a-zA-Z_];

fragment Digit: [0-9];

fragment NonZeroDigit: [1-9];

Skip: (([ \t\r\n]+) | ('//' .*?)) -> skip;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
