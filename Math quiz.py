import random

# Checks if the user enters yes(y) or no(n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

# instructions
def instructions():
    print("""


**** Instructions ****

To begin, choose the number of rounds /  questions you
would like to answer.

The game will generate questions for you to answer.      

Good luck.

    """)

def int_check(question, low=None, high=None, exit_code=None, infinite=""):

    while True:
        response = input(question).lower()

        # check for infinite / exit mode
        if response == exit_code:
            return response
        elif response == infinite:
            return response

        if response < "1":
            error = ("PLease enter an integer that is "
                     "more than / equals to 1")

        elif response != int:
            error = ("Please enter an integer")

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if response is valid, return it
            else:
                return response

        except ValueError:
            print(error)





# prints heading
print()
print("📚✖️➕➗🔢Welcome to the Math quiz⬇📚✖️➕➗🔢 ")
print()

# asks user if they want instruction
want_instructions = yes_no("Do you want to read the instructions? ")

# checks if user says yes
if want_instructions == "yes":
    instructions()

# ask user how many rounds they want
rounds = int_check("Rounds <enter> for infinite>: ", low=1)
# checks if infinite mode is chosen 
if rounds == "":
    mode = "infinite"
    rounds = 5
