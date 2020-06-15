# Charlie Conneely
# Score Keeper

from player import Player

class ScoreKeeper:
    def __init__(self):
        self.highscores = []

    def check_ranking(self, p):
        self.populate_ranks_array("rankings.txt")
        for p in self.highscores:
            print(p.name + " - " + str(p.score))

    def print_rankings(self):
        x=0
        print("\nNew Rankings:")
        for key, val in self.highscores:
            print(str(val)+" - "+str(key))
            x+=1
            if x==5: break

    def populate_ranks_array(self, scores_file):
        with open(scores_file) as f:
            for line in f:
                (n, s) = line.split()
                self.highscores.append(Player(n,s))

