# Charlie Conneely
# Score Keeper

from player import Player

class ScoreKeeper:
    def __init__(self):
        self.ranks = []

    def check_ranking(self, p):
        self.populate_ranks_array("rankings.txt")

        # check score against rankings
        self.compare_score(p)

        for p in self.ranks:
            print(p.name + " - " + str(p.score))

    def compare_score(self, player):
        does_rank = False
        for p in self.ranks:
            if (int(player.score) > int(p.score)):
                does_rank = True
        if does_rank:
            self.ranks.append(player)
            # sort array by ranks
            self.ranks.sort(key=lambda p: int(p.score), reverse=True)

    def populate_ranks_array(self, scores_file):
        with open(scores_file) as f:
            for line in f:
                (n, s) = line.split()
                self.ranks.append(Player(n,s))

