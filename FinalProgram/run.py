import sys, os
from utils import *

TARGET = '../CompiledLanguage'


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
