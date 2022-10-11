import os

TESTCASE_FOLDER = "./Testcases"
ANSWER_FOLDER = "./Answers"

if __name__ == "__main__":
    if not os.path.exists(ANSWER_FOLDER):
        os.mkdir(ANSWER_FOLDER)

    os.system("cd LanguageGenerator && python gen.py BKIT.g4")

    list_testcases = os.listdir(TESTCASE_FOLDER)
    list_testcases = list(filter(lambda x: x.endswith(".txt"), list_testcases))
    total_tc = len(list_testcases)

    for i, tc in enumerate(list_testcases):
        print("RUNNING %d/%d..." % (i + 1, total_tc))
        os.system(
            "cd FinalProgram && python run.py %s %s" % (
                '.' + os.path.join(TESTCASE_FOLDER, tc),
                '.' + os.path.join(ANSWER_FOLDER, tc)
            )
        )
