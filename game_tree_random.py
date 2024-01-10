import random

from game_engine import GameEngine, deep_copy_2d_array
from own_heap import OwnHeap
from constant import BOARD_SIZE, MAX_SCORE
from rule_random import RULE_RANDOM

# game_engine/ helper function
game_engine = GameEngine()


random.seed()


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

    def __init__(self, a_board, player, tree_height = 4):
        self.board = deep_copy_2d_array(a_board)
        self.player = player
        self.tree_height = tree_height

        self.rule = RULE_RANDOM()

        self.root = GameTree.Node(-1, -1, player, 0)
        self.create_children(self.root, self.board, player)

    def set_tree_board(self, a_board):
        self.board = deep_copy_2d_array(a_board)
        self.root.score = 0
        self.root.children = OwnHeap()
        self.create_children(self.root, self.board, self.player)


    def create_children(self, sub_tree, a_board, player):
        # layer 0 (root) and 1 are both the same player, 
        # player will be reversed in recursive function
        # thus in root create childern funtion player need to reverse
        self.recur_create_children(sub_tree, a_board, -1 * player, 0)

    def recur_create_children(self, parent_node, parent_board, parent_player, parent_depth):
        
        child_depth = parent_depth + 1
        child_player = parent_player * -1

        if child_depth >= self.tree_height:
            #print("depth: ", cur_depth, "player: ", cur_player)
            parent_node.score = self.rule.cal_score(parent_board, parent_player)
            return None

        elif game_engine.check_win(parent_board) == parent_player:
            score_sign = parent_depth % 2
            if score_sign == 0:
                score_sign = -1
            parent_node.score = MAX_SCORE * score_sign
            return None

        else:
            for x in range(BOARD_SIZE):
                for y in range(BOARD_SIZE):
                    child_board = game_engine.get_new_board(
                        parent_board, x, y, child_player)

                    if child_board is not None:
                        # print(x, y, "| ", child_board)
                        # print("----------")
                        new_child = GameTree.Node(
                            x, y, child_player, child_depth)
                        
                        #print("new_child depth: ", new_child.depth, "player ", new_child.player)

                        self.recur_create_children(
                            new_child, child_board, child_player, child_depth)

                        parent_node.children.ins(new_child)

            if len(parent_node.children.arr) > 0:
                if parent_depth % 2 == 0:
                    parent_node.children.heapify_max()
                else:
                    parent_node.children.heapify_min()                  

                # include random in choice
                randon_num_float = random.random()
                if randon_num_float <= 0.05 and len(parent_node.children.arr) > 2:
                    parent_node.score = parent_node.children.arr[2].score

                elif randon_num_float <= 0.2 and len(parent_node.children.arr) > 1:
                    parent_node.score = parent_node.children.arr[1].score

                else:
                    parent_node.score = parent_node.children.arr[0].score

    def get_best_move(self):
        # if game_engine.check_win(self.board, self.player) == 0:
        #     return (self.root.children.arr[0].move_x, self.root.children.arr[0].move_y)
        # else:
        #     return None
        if len(self.root.children.arr) > 0:
            return (self.root.children.arr[0].move_x, self.root.children.arr[0].move_y)
        else:
            return None


    def print(self):
        self.print_r(self.root)

    def print_r(self, subtree):        
        if subtree.children is not None:
            for elem in subtree.children.arr:
                self.print_r(elem)
        print(f"depth: {subtree.depth}, player: {subtree.player}, move: {subtree.move_x} {subtree.move_y}, score: {subtree.score}")
        
    def print_target_depth(self, target_d):
        self.print_td_r(self.root, target_d)

    
    def print_td_r(self, subtree, target_d):
        if subtree.children is not None:
            for elem in subtree.children.arr:
                self.print_td_r(elem, target_d)
        if subtree.depth == target_d:
            print(f"depth: {subtree.depth}, player: {subtree.player}, move: {subtree.move_x} {subtree.move_y}, score: {subtree.score}")
        
   
