from antlr4 import *
from lexererr import *


##### FOR LEXER #####
def checkLexeme(lexerAgent, inputFile, outputFile):
    dest = open(outputFile, "w")
    lexer = lexerAgent(FileStream(inputFile))
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


##### FOR PARSER #####
def checkParser(lexerAgent, parserAgent, inputFile, outputFile):
    dest = open(outputFile, "w")
    lexer = lexerAgent(FileStream(inputFile))

    tokens = CommonTokenStream(lexer)
    parser = parserAgent(tokens)

    try:
        tree = parser.program()
        dest.write("successful")

    except Exception as e:
        dest.write(str(e))
    finally:
        dest.close()

    dest = open(outputFile, "r")
    line = dest.read()
    print(line)
