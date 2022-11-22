import sys, os
from utils import *

TARGET_DIR = '../CompiledLanguage'
TESTCASE_DIR = '../Testcases'
ANSWER_DIR = '../Answers'
ASTTREE_DIR = '../ASTTrees'


def main(argv):
    if os.path.isdir(TARGET_DIR) and not TARGET_DIR in sys.path:
        sys.path.append(TARGET_DIR)
    from BKITLexer import BKITLexer
    from BKITParser import BKITParser

    if len(argv) < 2:
        file_name_list = os.listdir(TESTCASE_DIR)
        for file_name in file_name_list:
            if file_name.endswith(".txt"):
                astTree = checkAST(
                    BKITLexer, BKITParser, TESTCASE_DIR + "/" + file_name,
                    ANSWER_DIR + "/" + file_name
                )
                runCode(astTree, ASTTREE_DIR + "/" + file_name)
    elif len(argv) < 3:

        inputFile = argv[0]

        if len(argv) == 1:
            outputFile = "result.txt"
        else:
            outputFile = argv[1]

        astTree = checkAST(BKITLexer, BKITParser, inputFile, "asttree.txt")
        runCode(astTree, outputFile)

    else:
        printUsage()


def printUsage():
    print("python run.py TESTCASE_FILE [OUTPUT_FILE]")


if __name__ == "__main__":
    main(sys.argv[1:])
