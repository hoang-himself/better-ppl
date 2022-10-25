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

program: libIncl nsDef mainFunc EOF;

libIncl: libIncl libInclStmt |;

libInclStmt: Include InternalLib;

nsDef: nsDef nsDefStmt |;

nsDefStmt: Using NameSpace Id Semi;

mainFunc:;

Include: '#include';
If: 'if';
While: 'while';
Using: 'using';
NameSpace: 'namespace';
Cout: 'cout';
InternalLib: '<' (~['"\\\r\n>< ] | EscapeSequence)+ '>';
Int: 'int';
Flt: 'float';
Main: 'main';
Return: 'return';

Semi: ';';
OpenPara: '(';
ClosePara: ')';
OpenBraket: '{';
CloseBraket: '}';
Shift: '<<';
InEq: '>' | '<' | '>=' | '<=';
Inc: '++' | '--';
Eq: '==' | '!=';
Assignment: '=';

Id: NonDigit ( NonDigit | Digit)*;

Integer: Sign? ( NonZeroDigit Digit* | '0');

Float:
	Sign? (
		FragtionalConstant ExponentPart? FloatingPart?
		| DigitSequence ExponentPart FloatingPart?
	);

String:
	'"' SCharSequence? '"' {
      self.text = self.text[1:-1]
    };

Char:
	'\'' SCharChar '\'' {
      self.text = self.text[1:-1]
    };

fragment EscapeSequence: '\\' [bfrnt'"\\];

fragment IllegalEscapeSequence: '\\' ~[bfrnt'"\\];

fragment SCharSequence: SCharString+;

fragment SCharString: ~["\\\r\n] | EscapeSequence;

fragment SCharChar: ~['\\\r\n] | EscapeSequence;

fragment FragtionalConstant:
	DigitSequence '.' DigitSequence
	| DigitSequence '.';

fragment ExponentPart: [eE] Sign? DigitSequence;

fragment FloatingPart: 'f';

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
