# Charlie Conneely
# Score Keeper

class ScoreKeeper:
    def __init__(self):
        self.highscores = {}
        self.score = 0

    def increment_score(self, points):
        self.score = self.score + points
        return self.score

    def check_ranking(self, name):
        self.highscores = self.populate_scores_dict("rankings.txt")
        print(self.highscores)

    def populate_scores_dict(self, scores_file):
        scores = {}
        with open(scores_file) as f:
            for line in f:
                (key, val) = line.split()
                scores[int (key)] = val
        return scores
