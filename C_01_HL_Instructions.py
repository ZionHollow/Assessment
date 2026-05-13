# Checks users enter yes (yes) or no (n)

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

def instructions():
    print("""


**** Instructions ****
    
To begin, choose the number of rounds /  questions you
would like to answer.
    
The game will generate questions for you to answer.      
    
Good luck.
    
    """)


# Main routine
print()
print("📚✖️➕➗🔢Welcome to the Math quiz⬇📚✖️➕➗🔢 ")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

    # checks users enter yes (y) or no (n)
if want_instructions == "yes":
    print(instructions)
