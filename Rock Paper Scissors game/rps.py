import random

choice = ('r', 'p', 's')
comp = random.randint(0, 2)
comp = choice[comp]
mine = input("Enter your choice: Rock, Paper, Scissor\n")

def rps(comp, mine):
    if comp == mine:
        return None

    if comp == 'r' and mine == 'p':
        return True
    elif comp == 'p' and mine == 's':
        return True
    elif comp == 's' and mine == 'r':
        return True
    else:
        return False


win = rps(comp, mine)
print(f"You chose {mine} and computer chose {comp}")
if win is None:
    print("Match is Draw")

if win:
    print("You won")
else:
    print("You lose")
