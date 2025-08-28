import random
def guessing_game():
    num = random.randint(1,100)
    guess = None

    while guess != num:
        guess = int(input("Guess a number between 1 and 100 : "))

        if guess<num:
            print("Too Low! Try again.")
        elif guess>num:
            print("Too high! Try again")
        else:
            print("Congrats!You guessed the number")
guessing_game()

