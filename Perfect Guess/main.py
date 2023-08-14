from random import randint

class Guess:
    random = randint(1, 100)
    print(random)
    u1 = None
    guesses = 0
    
    while u1 != random:
        u1 = int(input("Enter a number between 1 to 100: "))
        if u1 == random:
            print("\n********You have guessed the correct number********\n")
        elif u1 > random:
            print("Lower number please")
        elif u1 < random:
            print("Higher number please")
        else:
            print("You guessed it wrong!")
        guesses += 1

    print(f"No. of guessess: {guesses}")

g = Guess()
