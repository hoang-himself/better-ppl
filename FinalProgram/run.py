import sys, os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from lexererr import *

TARGET = '../CompiledLanguage'


def checkLexeme(lexer, inputFile, outputFile):
    dest = open(outputFile, "w")
    lexer = lexer(FileStream(inputFile))
    try:
        out = printLexeme(lexer)
        dest.write(out)
    except LexerError as err:
        dest.write(err.message)
    finally:
        dest.close()

    # dest = open(outputFile,"r")
    # line = dest.read()
    # print("\"" + line + "\"")


def printLexeme(lexer):
    tok = lexer.nextToken()
    if tok.type != Token.EOF:
        return (lexer.symbolicNames[tok.type] + " " +
                printLexeme(lexer)).strip()
    else:
        return ""


class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException(
            "Error on line " + str(line) + " col " + str(column) + ": " +
            offendingSymbol.text
        )


NewErrorListener.INSTANCE = NewErrorListener()


class SyntaxException(Exception):
    def __init__(self, msg):
        self.message = msg


def checkParser(lexerAgent, parserAgent, inputFile, outputFile):
    dest = open(outputFile, "w")
    lexer = lexerAgent(FileStream(inputFile))
    listener = NewErrorListener.INSTANCE
    tokens = CommonTokenStream(lexer)
    parser = parserAgent(tokens)
    parser.removeErrorListeners()
    parser.addErrorListener(listener)

    try:
        parser.program()

    except SyntaxException as f:
        dest.write(f.message + '\n')
    except Exception as e:
        dest.write(str(e) + '\n')
    finally:
        dest.write("complete!")
        dest.close()

    # dest = open(outputFile,"r")
    # line = dest.read()
    # print(line)


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif len(argv) < 3:
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)

        from BKITLexer import BKITLexer
        from BKITParser import BKITParser

        inputFile = argv[0]

        if len(argv) == 1:
            outputFile = "result.txt"
        else:
            outputFile = argv[1]

        checkParser(BKITLexer, BKITParser, inputFile, outputFile)

    else:
        printUsage()


def printUsage():
    print("python run.py TESTCASE_FILE [OUTPUT_FILE]")


if __name__ == "__main__":
    main(sys.argv[1:])
