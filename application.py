import core.parse


def welcome():
    print("Welcome to MREPL")
    print("Use this at your own risk")
    print("Authors: Tarith Jayasooriya, Dinuda Yaggahavita")
    prompt()


def prompt():
    while True:
        inp = input()
        answer = "no answer"  # this variable will hold the answer of the input
        print(answer)


welcome()
