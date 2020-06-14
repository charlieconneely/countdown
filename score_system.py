# Charlie Conneely
# Score Keeper

class ScoreKeeper:
    def __init__(self):
        self.highscores = {}
        self.score = 0

    def increment_score(self, points):
        self.score += points
        return self.score

    def check_ranking(self, name):
        self.populate_scores_dict("rankings.txt")
        # intop5 = check top 5
       # self.highscores[self.score] = name

        for rank in self.highscores:
            print(rank)

    def populate_scores_dict(self, scores_file):
        x = 0
        with open(scores_file) as f:
            for line in f:
                (key, val) = line.split()
                self.highscores[int (key)] = val
                x+=1
                if x == 5:
                    break
            self.highscores  = sorted(self.highscores.items(),\
                    reverse=True)

    def check_top_five(self, rankings, score):
        isTopFive = False
        for key in rankings:
            if score > key:
                isTopFive = True
        return isTopFive

