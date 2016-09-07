# -*- coding: utf-8 -*-


class PPMatch:
    """Class to handle match data"""
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = [0, 0]
        return

    def setPoint(self, player):
        self.score[player] += 1
        return

    def getScore(self, player=-1):
        if player == -1:
            return tuple(self.score)
        else:
            return self.score[player]

    def haveWinner(self):
        if self.score[0] >= 21:
            return 0
        elif self.score[1] >= 21:
            return 1
        else:
            return -1