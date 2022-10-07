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

program:
	(
		(Include InternalLib)
		| If
		| While
		| Using
		| NameSpace
		| Cout
		| Int
		| Main
		| Return
		| Semi
		| OpenPara
		| ClosePara
		| OpenBraket
		| CloseBraket
		| Shift
		| InEq
		| Eq
		| Inc
		| Assignment
		| Id
		| Integer
		| Float
		| String
		| Char
	)* EOF;

Include: '#include';
InternalLib: '<' SCharSequence '>' {self.text = self.text[1:-1]};
If: 'if';
While: 'while';
Using: 'using';
NameSpace: 'namespace';
Cout: 'cout';
Int: 'int';
Main: 'main';
Return: 'return';

Semi: ';';
OpenPara: '(';
ClosePara: ')';
OpenBraket: '{';
CloseBraket: '}';
Shift: '<<' | '>>';
InEq: '<' | '>' | '<=' | '>=';
Inc: '++' | '--';
Eq: '==' | '!=';
Assignment: '=';

Id: NonDigit (NonDigit | Digit)*;

Float:
	FloatIntLiteral FloatDecLiteral
	| (FloatIntLiteral | FloatDecLiteral) FloatExpLiteral
	| FloatIntLiteral FloatDecLiteral FloatExpLiteral;
fragment FloatIntLiteral: Sign? Digit+;
fragment FloatDecLiteral: '.' Digit+;
fragment FloatExpLiteral: [Ee] Sign? Digit+;

Integer: Sign? Digit+;

String: '"' SCharSequence '"' {self.text = self.text[1:-1]};

Char: '\'' SChar '\'' {self.text = self.text[1:-1]};

fragment EscapeSequence: '\\' [bfrnt'"\\];
fragment IllegalEscapeSequence: '\\' ~[bfrnt'"\\];
fragment SCharSequence: SChar+;
fragment SChar: ~['"\\\r\n] | EscapeSequence;

fragment Sign: '+' | '-';

fragment DigitSequence: Digit+;

fragment NonDigit: [a-zA-Z_];

fragment Digit: [0-9];

fragment NonZeroDigit: [1-9];

Skip: (([ \t\r\n]+) | ('//' .*?)) -> skip;

ERROR_CHAR: .;

UNCLOSE_STRING:
	'"' SCharSequence? {
      self.text = self.text[1:]
    };
ILLEGAL_ESCAPE:
	'"' SCharSequence? IllegalEscapeSequence {
      self.text = self.text[1:]
    };
UNTERMINATED_COMMENT: .;
