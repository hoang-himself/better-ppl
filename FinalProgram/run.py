import sys, os
from antlr4 import *
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

    dest = open(outputFile, "r")
    line = dest.read()
    print(line)


def printLexeme(lexer):
    tok = lexer.nextToken()
    if tok.type != Token.EOF:
        return (
            "<" + lexer.symbolicNames[tok.type] + ", \"" + tok.text + "\">\n" +
            printLexeme(lexer)
        ).strip()
    else:
        return ""


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif len(argv) < 3:
        if os.path.isdir(TARGET) and not TARGET in sys.path:
            sys.path.append(TARGET)

        from BKITLexer import BKITLexer

        inputFile = argv[0]

        if len(argv) == 1:
            outputFile = "result.txt"
        else:
            outputFile = argv[1]

        checkLexeme(BKITLexer, inputFile, outputFile)

    else:
        printUsage()


def printUsage():
    print("python run.py TESTCASE_FILE [OUTPUT_FILE]")


if __name__ == "__main__":
    main(sys.argv[1:])
