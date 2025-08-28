import random
def number_guesser():
    start = int(input("Enter the starting range : "))
    end = int(input("Enter the ending range : "))

    number = random.randint(start,end)
    guess = None

    while guess!=number:
        guess = int(input(f"Guess a number between {start} and {end}: "))

        if guess<number:
            print("Too low! Try again")
        elif guess >number:
            print("Too high! Try again")
        else:
            print("Correct! The Number is ",number)
number_guesser()