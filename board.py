import pygame

from game_engine import GameEngine
from constant import BOARD_SIZE, GRID_SIZE, COLOR


class Board:
    def __init__(self, screen, cur_player):
        # TBD: add list to store a few step instead of just one board
        self.board = [[0] * BOARD_SIZE for _ in range(BOARD_SIZE)]
        self.board[3][3], self.board[4][4] = 1, 1
        self.board[3][4], self.board[4][3] = -1, -1
        self.screen = screen
        self.cur_player = cur_player

        self.game_engine = GameEngine()

    def get_cur_player(self):
        return self.cur_player

    def get_cur_board(self):
        # print(self.board)
        return self.board

    # draw the board
    def draw(self):
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                # draw the rectangle
                a_grid = pygame.Rect(row*GRID_SIZE, col *
                                     GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, "black", a_grid, 1)

                # draw the chess if data exist in that grid
                player_data = self.board[row][col]
                # print(player)
                if player_data != 0:
                    chess_pos = pygame.Vector2(
                        col * GRID_SIZE + GRID_SIZE // 2, row*GRID_SIZE + GRID_SIZE // 2)
                    pygame.draw.circle(
                        self.screen, COLOR[player_data == 1], chess_pos, GRID_SIZE // 2 - 10)

        # TBS: draw player info

    # handle player mouse click
    def handle_mouse_click(self, mouse_pos):
        # only response if the click is inside the board
        # TBD: add offset
        if mouse_pos[0] <= BOARD_SIZE * GRID_SIZE and mouse_pos[1] <= BOARD_SIZE * GRID_SIZE:
            row = mouse_pos[1] // GRID_SIZE
            col = mouse_pos[0] // GRID_SIZE
            # check if it is a valid move
            grid_change = self.game_engine.check_move(
                self.board, row, col, self.cur_player)
            if grid_change is not None:
                # if valid, change the corresponding grid
                self.board[row][col] = self.cur_player
                for elem in grid_change:
                    self.board[elem[0]][elem[1]] = self.cur_player

                # check if the other player have valid move, if yes, change to other player turns
                if self.game_engine.check_moves_exist(self.board, self.cur_player * -1):
                    self.cur_player *= -1

    def handle_move(self, x, y):

        new_board = self.game_engine.get_new_board(
            self.board, x, y, self.cur_player)
        self.board = new_board
        if self.game_engine.check_moves_exist(self.board, self.cur_player * -1):
            self.cur_player *= -1
            
    # return None if game is to be continue
    # return 1 if player 1 (repsented by 1 in array) win, 
    # return -1 when player 2 (represented by -1 in array) win, 
    # return 0 when tie
    def check_win(self):
        return self.game_engine.check_win(self.board)
