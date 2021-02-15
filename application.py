import core.parse


def main():
    welcome()
    prompt()


def welcome():
    print("Welcome to MREPL")
    print("Use this at your own risk")
    print("Authors: Tarith Jayasooriya, Dinuda Yaggahavita")


def prompt():
    while True:
        inp = input()
        answer = "no answer"  # this variable will hold the answer of the input
        print(answer)


main()
