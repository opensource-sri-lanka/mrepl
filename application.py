import core.parse


def main():
    welcome()
    prompt()


def welcome():
    print("Welcome to MREPL")
    print("Use this at your own risk")
    print("Authors: Tarith Jayasooriya, Dinuda Yaggahavita")
    print("")  # leave a space


def prompt():
    print("Enter your equation: ")
    # Hold the input
    inp = input()
    # Checks if the input is valid
    if (len(inp) > 0):
        # find the operators
        add = inp.find("+")
        if(add > 0):
            print("Has addition")
        else:
            print("No addition")
    else:
        print("Please enter a valid equation")
        prompt()


main()
