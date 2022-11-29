from antlr4 import *
from lexererr import *
from stack import env


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
            "<" + lexer.symbolicNames[tok.type] + ', "' + tok.text + '">\n' +
            printLexeme(lexer)
        ).strip()
    else:
        return ""


##### FOR PARSER & AST #####
def checkAST(lexerAgent, parserAgent, inputFile, outputFile):
    dest = open(outputFile, "w")
    lexer = lexerAgent(FileStream(inputFile))

    tokens = CommonTokenStream(lexer)
    parser = parserAgent(tokens)
    asttree = None

    try:
        tree = parser.program()
        # Now tree is an instance of BKITParser.ProgramContext

        from ASTGeneration import ASTGeneration

        ast_generator = ASTGeneration()

        # Because BKITParser.ProgramContext has implemented Visitor pattern with accept method,
        # We can call tree.accept(ast_generator) to build our AST.
        asttree = tree.accept(ast_generator)

        dest.write(str(asttree))

    except Exception as e:
        dest.write(str(e))
    finally:
        dest.close()

    dest = open(outputFile, "r")
    line = dest.read()
    print("AST Tree:", line)

    return asttree


def runCode(astTree, outputFile):
    dest = open(outputFile, "w")

    try:
        from CodeRunner import CodeRunner

        code_runner = CodeRunner()
        result = astTree.accept(code_runner)
        dest.write(result)

    except Exception as e:
        dest.write(str(e))
    finally:
        dest.close()

    dest = open(outputFile, "r")
    line = dest.read()
    print("Result:", line)


class Env:
    _env = env

    @classmethod
    def get(cls, name):
        return cls._env[name]


def lookup(string):
    return Env.get(string)
