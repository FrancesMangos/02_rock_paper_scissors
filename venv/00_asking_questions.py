# functions go here

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 30\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            #if the amount is too low or too high
            if low < response <= high:
                return response


            #output an error
            else:
                print(error)

        except ValueError:
            print(error)


def gamemode(question):
    valid = False
    while not valid:
        response = input("Would you like to play with a set amount of "
                         "rounds or infinite amount of rounds?(Type set or infinite)").lower()


        if response == "set":
            response = "set"
            return response

        # If input no, display instructions
        elif response == "infinite":
            response = "infinite"
            return response

        #If input not yes or no, clarify question
        else:
            print("<error> please insert set or infinite")


def yes_no_instructions(question):
    valid = False
    while not valid:
        answer = input("Would you like to see the instructions for the gamemode?").lower()


        if answer == "y" or answer == "yes":
            answer = "yes"
            return answer

        # If input no, display instructions
        elif answer == "no" or "n":
            answer = "no"
            return answer

        #If input not yes or no, clarify question
        else:
            print("<error> please insert yes or no")


def set_gamemode():
    print("These are the instructions for the set rounds gamemode:")
    print("You will be asked to insert a number between 1 and 30, this will be how many rounds you will play")
    print("Then, you will be asked to insert a number between 1 and whatever number you inserted before, this will be the winning round number")
    print("The first player to win as many rounds as the winning round number wins the game")
    print("If both players do not reach the winning round number, the game ends in a tie")
    print("At the end of the game")
def infinite_gamemode():
    print("Instructions for the infinite rounds gamemode")


# main routine goes here
print("Welcome to The Rock Paper Scissors Game!")
gamemode_chosen = gamemode("Would you like to play with a set amount of "
                           "rounds or infinite amount of rounds?(Type set or infinite)")


if gamemode_chosen == "set":
    want_instructions = yes_no_instructions("Would you like to see the instructions?")
    if want_instructions == "yes":
        set_gamemode()
    print()
    rounds_wanted = num_check("How many rounds would you like to play?", 0, 30)

    print("You want to play {} rounds!".format(rounds_wanted))
    print()
    final_score = num_check("How many rounds does a player need to win to win "
                                    "the whole game?(Between 1 and how many rounds you chose to win the game)", 0, rounds_wanted)

    print("You chose that a player needs to win {} rounds out of {} to win the whole game!".format(final_score, rounds_wanted) )

elif gamemode_chosen == "infinite":
    want_instructions = yes_no_instructions("Would you like to see the instructions?")
    if want_instructions == "yes":
        infinite_gamemode()
    print()
    print("why")

else:
    print("why")
