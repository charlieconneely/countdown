# Charlie Conneely
# Score Keeper

from player import Player

ranks_file = "rankings.txt"

class ScoreKeeper:

    def __init__(self):
        self.ranks = []

    def check_ranking(self, p):
        self.populate_ranks_array(ranks_file)

        # check score against rankings
        top5 = self.compare_score(p)

        if top5:
            print("New Rankings:")
            for p in self.ranks:
                print(p.name + " - " + str(p.score))

        self.append_file(ranks_file)
        self.ranks = []

    def append_file(self, rfile):
        with open(rfile, 'w') as file:
            for p in self.ranks:
                file.write(str(p.name) + " " + str(p.score) + "\n")

    def compare_score(self, player):
        does_rank = False
        for p in self.ranks:
            if (int(player.score) > int(p.score)):
                does_rank = True
        if does_rank:
            self.ranks.append(player)
            # sort ranks array by scores
            self.ranks.sort(key=lambda p: int(p.score), reverse=True)
            # remove the last item
            self.ranks.pop()
        return does_rank

    def populate_ranks_array(self, scores_file):
        with open(scores_file) as f:
            for line in f:
                (n, s) = line.split()
                self.ranks.append(Player(n,s))

