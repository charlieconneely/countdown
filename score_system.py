# Charlie Conneely
# Score Keeper

class ScoreKeeper:
    def __init__(self):
        self.highscores = []
        self.score = 0

    def increment_score(self, points):
        self.score = self.score + points
        return self.score

