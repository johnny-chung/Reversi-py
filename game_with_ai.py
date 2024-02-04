
import pygame
import time

from board import Board
from game_tree import GameTree
from nn_ai import REVERSI_AI

from constant import GRID_SIZE

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
board = Board(screen, 1)
ai = REVERSI_AI()

while running:

    mouse_pos = None
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    font = pygame.font.Font(None, 36)
    inner_text = None

    if board.get_cur_player() == 1:
        if mouse_pos is not None:
            board.handle_mouse_click(mouse_pos)
    else:
        moves = ai.get_move(board.get_cur_board(), -1)
        if moves is None:
            print("ai fail")
            computer = GameTree(board.get_cur_board(), -1)
            moves = computer.get_best_move()
        print("actual move: ", moves)
        time.sleep(1)
        if moves is not None:
            board.handle_move(moves[0], moves[1])

    board.draw()

    if board.get_cur_player() == 1:
        inner_text = "Player"
    else:
        inner_text = "Computer"
    screen.blit(font.render(inner_text, 1, "black"), (8 * GRID_SIZE + 5, 5))

    win = board.check_win()
    if win is not None:
        text = None
        if win == 1:           
            text = "White Win"            
        elif win == -1:
            text = "Black Win"                   


        screen.blit(font.render(text, 1, "black"), (8 * GRID_SIZE + 5, 50))
        running = False


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

time.sleep(2)
pygame.quit()
