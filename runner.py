# Charlie Conneely
# Anagram game

from countdown import Countdown
from score_system import ScoreKeeper

countdown = Countdown()
score_keeper = ScoreKeeper()

def main(name):
    rounds = 2
    score_keeper.score = 0

    print("\nWe're going for best of "+str(rounds)+" rounds!")
    print("At the moment the high score is 2000! Good luck!\n")

    for x in range(rounds):
        points = countdown.play_countdown(name)
        score_keeper.score = score_keeper.increment_score(points)

    score_keeper.check_ranking(name)

    print("Score: " + str(score_keeper.score))

def intro():
    name = str(input("Enter your name here: "))
    print("\nWelcome "+name+"!\nLet's Play Countdown!!\n")
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

