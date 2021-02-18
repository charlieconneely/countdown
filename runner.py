# Charlie Conneely
# Anagram game

from countdown import Countdown
from score_system import ScoreKeeper
from player import Player

countdown = Countdown()
score_keeper = ScoreKeeper()

"""
Call play_countdown in Countdown class
Keep track of score
Check rankings
"""
def main(name):
    rounds = 3
    player = Player(name, 0)

    print("\nWe're going for best of "+str(rounds)+" rounds!")

    for x in range(rounds):
        points = countdown.play_countdown(player.name)
        player.score += points

    print("Total Score: " + str(player.score) + "\n")
    score_keeper.check_ranking(player)

"""
Introduce game and collect player name 

returns String - Player name
"""
def intro():
    name = str(input("Enter your name here: "))
    print("Welcome "+name+"!\nLet's Play Countdown!!\n")
    return name

if __name__ == "__main__":
    name = intro()
    ready_to_play = True
    while True:
        if ready_to_play:
            main(name)

        choice = input("\nWould you like to play again? (y/n):")
        choice = choice.lower()
        if choice not in ["y", "n"]:
            ready_to_play = False
            print("Invalid input. Please try again.")
        elif (choice == 'y'):
            ready_to_play = True
        else:
            break

