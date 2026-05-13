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

To begin, choose the number of total_questions /  questions you
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
            error = "Please enter an integer"

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
def ans_check(question, exit_code = "xxx"):

    # checks if the response is the exit code
    while True:
        response = input(question).lower()
        if response == exit_code:
            return response
        # checks if the response is an integer
        try:
            integer = float(response)
            return integer

        except ValueError:
            print("Please enter an integer")

# variables

operator_list = "+", "-", "*", "/"
questions_answered = 0
mode = "regular"
quiz_history = []
Statistics = ""
correct_answer = 0
Incorrect_answer = 0


# prints heading
print()
print("📚✖️➕➗🔢Welcome to the Math quiz⬇📚✖️➕➗🔢 ")
print()

# asks user if they want instruction
want_instructions = yes_no("Do you want to read the instructions? ")

# checks if user says yes
if want_instructions == "yes":
    instructions()

# ask user how many total_questions they want
total_questions = int_check("Rounds <enter> for infinite>: ", low=1)
# checks if infinite mode is chosen 
if total_questions == "":
    mode = "infinite"
    total_questions = 5

while total_questions > questions_answered:
    # Round Heading
    if mode == "infinite":
        print(f"--- Question number {questions_answered + 1} (infinite mode) ---")
    else:
        print(f"--- Question number {questions_answered + 1} ---")
    # Variables that choose a number from 1 to 100 and chooses operator symbol
    num1 = random.randint(1,100)
    num2 = random.randint(1, 100)
    operator = random.choice(operator_list)

    print()

    # Finds the Answer to the generated question
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    elif operator == "*":
        answer = num1 * num2
    else:
        answer = num1 / num2
    # Rounds answer to the nearest integer
    answer = round(answer,2)
    print(answer)

    # generates question
    response = ans_check(f"{num1} {operator} {num2} =")

    # checks if user ends the quiz
    if response == "xxx":
        print("You quit the quiz and did not want to answer any rounds")
        break


    # total_questions the response
    response = round(response, 2)
    # shows the user if the answer is correct or Incorrect
    if response == answer:
        feedback = "correct"
        print(feedback)

        correct_answer += 1
    else:
        feedback = "Incorrect"
        print(feedback)
        Incorrect_answer += 1

    quiz_history.append(f"{num1} {operator} {num2} = {answer} | User response: {feedback}")
    # Adds another question to total_questions played
    questions_answered += 1

    # If mode is infinite it adds the round by +1 everytime
    if mode == "infinite":
        total_questions += 1



if questions_answered > 0:
    # Output the statistics
    statistics = f"""\n👔👔👔 Statistics 👔👔👔
    correct answers: {correct_answer} | Incorrect answers: {Incorrect_answer} | Percentage of correct answers {correct_answer/questions_answered*100}"""
    print(statistics)

    want_history = yes_no("Do you want to see quiz history")
    if want_history == "yes":
        print(quiz_history)







