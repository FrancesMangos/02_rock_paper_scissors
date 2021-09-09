# functions go here

def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 20\n"

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


# main routine goes here
print("Welcome to The Rock Paper Scissors Game!")
gamemode_chosen = gamemode("Would you like to play with a set amount of "
                           "rounds or infinite amount of rounds?(Type set or infinite)")


if gamemode_chosen == "set":
    rounds_wanted = num_check("How many rounds would you like to play?", 0, 20)

    print("You want to play {} rounds!".format(rounds_wanted))
    print()
    final_score = num_check("How many rounds does a player need to win to win "
                                    "the whole game?(Between 1 and how many rounds you chose to win the game)", 1, rounds_wanted)

    print("You chose that a player needs to win {} rounds out of {} to win the whole game!".format(final_score, rounds_wanted) )

elif gamemode_chosen == "infinite":
    print("why")

else:
    print("why")

