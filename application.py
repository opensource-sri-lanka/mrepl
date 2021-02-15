import core.parse


def main():
    welcome()
    prompt()


def welcome():
    print("Welcome to MREPL")
    print("Use this at your own risk")
    print("Authors: Tarith Jayasooriya, Dinuda Yaggahavita")


def prompt():
    print("Enter your equation: ")
    # Hold the input
    inp = input()
    if (len(inp) > 0):
        # find the operators
        print("input detected")
    else:
        print("Please enter a valid equation")
        prompt()


main()
