import random
import sys


class Results:
    # record user input
    def __init__(self):
        user_input = input("Pick R, P, or S?")

        self.selection = user_input

    def output(self):
        # return cpu output and run through the game

        cpu_output = random.choice(("R", "P", "S"))

        if self.selection == cpu_output:
            print(f"TIE")
        elif self.selection == "R":
            if cpu_output == "P":
                print(
                    f" Player(Rock): Computer(Paper) Paper beats rock. COMP won this round"
                )
            else:
                print(f"Rock beats scissors. PLAYER won this round")
        elif self.selection == "P":
            if cpu_output == "S":
                print(
                    f" Player(paper): Computer(Scissors) Scissors beats Paper. COMP won this round"
                )
            else:
                print(f" Paper beats Rock . PLAYER won this round")
        elif self.selection == "S":
            if cpu_output == "R":
                print(
                    f" Player(Scissors): Computer(Rock) Rock beats Scissors. COMP won this round"
                )
            else:
                print(f" Scissors beats Paper.  PLAYER won this round")

    def restart(self):
        # allow user to restart the game

        game_reset = input("Would you like to play again?")
        if game_reset == "Yes" or "yes":
            print(f"Starting up a new game")
            self.output()
        else:
            print(f"Exiting the game. Thanks for playing {User_name}")
            sys.exit()


while True:
    result = Results()
    result.output()
    result.restart()
