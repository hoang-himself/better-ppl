import sys, os
import subprocess

# Make sure that ANTLR_JAR is set to antlr-4.9.2-complete.jar
ANTLR_JAR = os.environ.get('ANTLR_JAR')
TARGET = '../CompiledLanguage'


def main(argv):

    if len(argv) < 1:
        printUsage()

    elif argv[0].endswith(".g4"):
        LANG_DEF = argv[0]

        subprocess.run(
            [
                "java", "-jar", ANTLR_JAR, "-o", TARGET, "-no-listener",
                "-visitor", LANG_DEF
            ]
        )

    elif argv[0] == 'clean':
        subprocess.run(["rm", "-rf", TARGET])

    else:
        printUsage()


def printUsage():
    print("python gen.py LANGUAGE.g4")


if __name__ == "__main__":
    main(sys.argv[1:])
