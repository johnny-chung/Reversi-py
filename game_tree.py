from game_engine import GameEngine, deep_copy_2d_array
from own_heap import OwnHeap
from constant import BOARD_SIZE, MAX_SCORE
from ai import AI

# game_engine/ helper function
game_engine = GameEngine()
ai = AI()


class GameTree:
    class Node:
        def __init__(self, move_x, move_y, player, depth, score=0):
            self.move_x = move_x
            self.move_y = move_y
            self.player = player
            self.depth = depth
            self.score = score
            self.children = OwnHeap()

        # custom operator overload for comparison in heap
        def __lt__(self, other):
            return self.score < other.score

        def __gt__(self, other):
            return self.score > other.score

        def __le__(self, other):
            return self.score <= other.score

        def __ge__(self, other):
            return self.score >= other.score

        def __eq__(self, other):
            return self.score == other.score

        def __ne__(self, other):
            return self.score != other.score

    def __init__(self, a_board, player, tree_height=4):
        self.board = deep_copy_2d_array(a_board)
        self.player = player
        self.tree_height = tree_height

        self.root = GameTree.Node(-1, -1, player, 0)

        self.create_children(self.root, self.board, player)

    def create_children(self, sub_tree, a_board, player):
        depth = 0
        self.recur_create_children(sub_tree, a_board, player, depth)

    def recur_create_children(self, parent_node, parent_board, cur_player, cur_depth):

        if cur_depth >= self.tree_height:
            parent_node.score = ai.cal_score(parent_board, cur_player)
            return None

        elif game_engine.check_win(parent_board, cur_player) == 1:
            parent_node.score = MAX_SCORE
            return None

        else:
            for x in range(BOARD_SIZE):
                for y in range(BOARD_SIZE):
                    child_board = game_engine.get_new_board(
                        parent_board, x, y, cur_player)
                    
                    if child_board is not None:
                        # print(x, y, "| ", child_board)
                        # print("----------")       
                        new_child = GameTree.Node(x, y, cur_player, cur_depth + 1)

                        self.recur_create_children(
                            new_child, child_board, cur_player * -1, cur_depth + 1)

                        parent_node.children.ins(new_child)

            if len(parent_node.children.arr) > 0:
                if cur_depth % 2:
                    parent_node.children.heapify_max()
                else:
                    parent_node.children.heapify_min()
                
                parent_node.score = parent_node.children.arr[0].score

    def get_best_move(self):
        # if game_engine.check_win(self.board, self.player) == 0:
        #     return (self.root.children.arr[0].move_x, self.root.children.arr[0].move_y)
        # else:
        #     return None
        if self.root.children is not None:
            return (self.root.children.arr[0].move_x, self.root.children.arr[0].move_y)
        else:
            return None