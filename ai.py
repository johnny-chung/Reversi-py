from game_engine import GameEngine
from constant import BOARD_SIZE, MAX_SCORE

game_engine = GameEngine()


class AI:
    def cal_score(self, a_board, player):
        if game_engine.check_win(a_board, player) == 1:
            return MAX_SCORE

        player_1_score, player_2_score = 0, 0

        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if a_board[x][y] is not None:
                    if a_board[x][y] > 0:
                        player_1_score += 1
                    else:
                        player_2_score += 1

        if player > 0:
            return player_1_score
        else:
            return player_2_score
