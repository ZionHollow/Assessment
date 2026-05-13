import random

def ans_check(question):

    while True:
        response = input(question)
        try:
            integer = int(response)
            return integer

        except ValueError:
            print("Please enter an integer")


num1 = random.randint(0,100)
num2 = random.randint(0, 100)
symbols= ["+", "-", "*", "/"]
random_symbol = random.choice(symbols)

print()


if random_symbol == "+":
    answer = num1 + num2
elif random_symbol == "-":
    answer = num1 - num2
elif random_symbol == "*":
    answer = num1 * num2
else:
    answer = num1 / num2

answer = round(answer,0)
print(answer)

response = ans_check(f"{num1} {random_symbol} {num2} =")
response = round(response,0)



while response != answer:
    print("Your answer is incorrect. Please try again")
    print(answer)
    response = ans_check(f"{num1} {random_symbol} {num2} =")
    response = round(response, 0)

print("Your answer is correct!")