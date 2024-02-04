import random

from game_engine import GameEngine
from constant import BOARD_SIZE, MAX_SCORE


game_engine = GameEngine()

random.seed()

class RULE_RANDOM:
    def __init__(self):
        self.factor_a = random.randint(0, 2)
        self.factor_b = random.randint(0, 2)
        self.factor_c = random.randint(0, 2)

    def check_grid_score(self, x, y, a_board, player):
        score = 6

        if x == 0 or x == 7:
            score += (1 + self.factor_a)
            if y == 0 or y == 7:
                score += 20
        elif x == 1 or x == 6:
            score -= (20 + self.factor_b)
            if y == 1 or y == 6:
                score -= 120
        elif x == 2 or x == 5:
            score += (3 + self.factor_c)

        if y == 0 or y == 7:
            score += (1 + self.factor_a)          
        elif y == 1 or y == 6:
            score -= (20 + self.factor_b)
        elif y == 2 or y == 5:
            score += (3 + self.factor_c)

        if x == 3 or x == 4:
            if y == 0 or y == 7:
                if a_board[x-1][y] == -player:
                    score -= (25 - self.factor_a)
                if a_board[x+1][y] == -player:
                    score -= (25 - self.factor_a)

        if y == 3 or y == 4:
            if x == 0 or x == 7:
                if a_board[x][y-1] == -player:
                    score -= (25 - self.factor_a)
                if a_board[x][y+1] == -player:
                    score -= (25 - self.factor_a)

        return score

    def cal_score(self, a_board, player):
        if game_engine.check_win(a_board) == player:
            return MAX_SCORE

        player_1_score, player_2_score = 0, 0
        zero_score = 0

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if a_board[x][y] > 0:
                    player_1_score += self.check_grid_score(x, y, a_board, 1)
                elif a_board[x][y] < 0:
                    player_2_score += self.check_grid_score(x, y, a_board, -1)
                else:
                    zero_score += 5

        if player > 0:
            return player_1_score - player_2_score + zero_score
        else:
            return player_2_score - player_1_score + zero_score
