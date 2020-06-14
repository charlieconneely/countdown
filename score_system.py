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
        x=0
        self.populate_scores_dict("rankings.txt")
        # check if current score ranks in the top 5
        intop5 = self.check_top_five()
        # if true, append/overwrite to that position
        if intop5:
            self.highscores[int(self.score)] = str(name)
            self.highscores = sorted(self.highscores.items(), reverse=True)
            print("\nNew Rankings:")
            for key, val in self.highscores:
                print(str(val)+" - "+str(key))
                x+=1
                if x==5: break
            # append text file with new dictionary

    def populate_scores_dict(self, scores_file):
        x = 0
        with open(scores_file) as f:
            for line in f:
                (key, val) = line.split()
                self.highscores[int (key)] = val
                x+=1
                if x == 5:
                    break

    def check_top_five(self):
        isTopFive = False
        for key, val in self.highscores.items():
            if self.score > int(key):
                isTopFive = True
        return isTopFive

