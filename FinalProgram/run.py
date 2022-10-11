import importlib
import sys, os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener, ErrorListener
from lexererr import *

TARGET_DIR = '../CompiledLanguage'
TESTCASE_DIR = '../Testcases'
ANSWER_DIR = '../Answers'


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


def main(*args, **kwargs):
    if len(args) < 1:
        printUsage()
    elif len(args) < 4:
        if os.path.isdir(TARGET_DIR) and not TARGET_DIR in sys.path:
            sys.path.append(TARGET_DIR)
        # Not the best I can do but I don't care
        LANGUAGE_NAME = args[0][0][:-3]

        MyLexer = getattr(
            importlib.import_module(LANGUAGE_NAME + "Lexer"),
            LANGUAGE_NAME + "Lexer"
        )
        MyParser = getattr(
            importlib.import_module(LANGUAGE_NAME + "Parser"),
            LANGUAGE_NAME + "Parser"
        )

        # TODO Split lexeme and parser tests
        if len(args) == 1:
            file_name_list = os.listdir(TESTCASE_DIR)
            for file_name in file_name_list:
                if file_name.endswith(".txt"):
                    checkParser(
                        MyLexer, MyParser, TESTCASE_DIR + "/" + file_name,
                        ANSWER_DIR + "/" + file_name
                    )
        else:
            inputFile = args[1]
            if len(args) == 2:
                outputFile = "result.txt"
            else:
                outputFile = args[2]
            checkParser(MyLexer, MyParser, inputFile, outputFile)

    else:
        printUsage()


def printUsage():
    print("python run.py LANGUAGE.g4 [TESTCASE_FILE [OUTPUT_FILE]]")


if __name__ == "__main__":
    main(sys.argv[1:])
