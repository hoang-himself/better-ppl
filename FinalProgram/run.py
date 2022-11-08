import importlib
import sys, os
from utils import *

TARGET_DIR = '../CompiledLanguage'
TESTCASE_DIR = '../Testcases'
ANSWER_DIR = '../Answers'


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif len(argv) < 4:
        if os.path.isdir(TARGET_DIR) and not TARGET_DIR in sys.path:
            sys.path.append(TARGET_DIR)
        if (argv[0][0][-3:] != '.g4'):
            print("Not a .g4 file")
            return 1
        LANGUAGE_NAME = argv[0][0][:-3]

        MyLexer = getattr(
            importlib.import_module(LANGUAGE_NAME + "Lexer"),
            LANGUAGE_NAME + "Lexer"
        )
        MyParser = getattr(
            importlib.import_module(LANGUAGE_NAME + "Parser"),
            LANGUAGE_NAME + "Parser"
        )

        if len(argv) == 1:
            file_name_list = os.listdir(TESTCASE_DIR)
            for file_name in file_name_list:
                if file_name.endswith(".txt"):
                    checkAST(
                        MyLexer, MyParser, TESTCASE_DIR + "/" + file_name,
                        ANSWER_DIR + "/" + file_name
                    )
        else:
            inputFile = argv[1]
            if len(argv) == 2:
                outputFile = "result.txt"
            else:
                outputFile = argv[2]
            checkAST(MyLexer, MyParser, inputFile, outputFile)
    else:
        printUsage()


def printUsage():
    print("python run.py LANGUAGE.g4 [TESTCASE_FILE [OUTPUT_FILE]]")
    return 1


if __name__ == "__main__":
    main(sys.argv[1:])
