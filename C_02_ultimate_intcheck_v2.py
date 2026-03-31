


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


# Main Routine goes here


    rounds = int_check("Rounds <enter> for infinite>: ", low=1)
    if rounds == "":
        print("You asked for infinite mode")
    else:
        print(f"you asked for {rounds}")



