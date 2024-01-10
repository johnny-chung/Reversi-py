
import pygame
import time

from board import Board
from game_tree_random import GameTree
from game_engine import GameEngine, deep_copy_2d_array

import pandas as pd
import numpy as np

from constant import BOARD_SIZE, GRID_SIZE

# pygame setup

def write_to_csv(file_path, py_array):
    np_array = np.array(py_array)
    new_df = pd.DataFrame([np_array .flatten()])
    new_df.to_csv(file_path, mode='a', header=False, index=False)


def flip_board(array):
    new_board = deep_copy_2d_array(array)
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if new_board[i][j] != 0:
                new_board[i][j] *= -1
    return new_board


count = 0

while count < 50:

    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    board = Board(screen, 1)
    computer_1 = GameTree(board.get_cur_board(), 1)
    computer_2 = GameTree(board.get_cur_board(), -1)


    ai_1_inputs = []
    ai_1_outputs = []
    ai_2_inputs = []
    ai_2_outputs = []


    while running:

        # mouse_pos = None
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        font = pygame.font.Font(None, 36)
        inner_text = None

        if board.get_cur_player() == 1:
            computer_1.set_tree_board(board.get_cur_board())
            
            moves = computer_1.get_best_move()
            if moves is not None:

                input_board = deep_copy_2d_array(board.board)
                ai_1_inputs.append(input_board)

                # output_board = deep_copy_2d_array(input_board)
                # output_board[moves[0]][moves[1]] = 1
                # ai_1_outputs.append(output_board)

                ai_1_outputs.append((moves[0], moves[1])) 

                board.handle_move(moves[0], moves[1])
        else:
            computer_2.set_tree_board(board.get_cur_board())
            moves = computer_2.get_best_move()
            if moves is not None:

                input_board = flip_board(board.board)
                ai_2_inputs.append(input_board)

                # output_board = deep_copy_2d_array(input_board)
                # output_board[moves[0]][moves[1]] = 1
                # ai_2_outputs.append(output_board) 

                ai_2_outputs.append((moves[0], moves[1])) 

                board.handle_move(moves[0], moves[1])

        board.draw()

        # if board.get_cur_player() == 1:
        #     inner_text = "Player"
        # else:
        #     inner_text = "Computer"
        # screen.blit(font.render(inner_text, 1, "black"), (8 * GRID_SIZE + 5, 5))

        win = board.check_win()
        if win is not None:
            boards_csv = 'input.csv'
            moves_csv = 'output.csv'
            text = None
            if win == 1:           
                text = "White Win"
                for i in range(len(ai_1_inputs)):
                    write_to_csv(boards_csv, ai_1_inputs[i])
                    write_to_csv(moves_csv, ai_1_outputs[i])
            elif win == -1:
                text = "Black Win"
                for i in range(len(ai_2_inputs)):
                    write_to_csv(boards_csv, ai_2_inputs[i])
                    write_to_csv(moves_csv, ai_2_outputs[i])           


            screen.blit(font.render(text, 1, "black"), (8 * GRID_SIZE + 5, 50))
            running = False


        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

    #time.sleep(5)
    count += 1
    
pygame.quit()
