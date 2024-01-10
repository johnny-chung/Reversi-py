
import unittest
from game_tree import GameTree
from export_csv import ExportCSV

export_csv = ExportCSV('sample_move.csv')


class GameTreeTestCase(unittest.TestCase):
    """These are the test cases for functions and classes of game tree"""

    def test_gametree(self):

        boards = [[
            # a board that is one move away from winning for p1
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0, -1,  0,  0,  0,  0],
            [0,  0,  0, -1,  1,  0,  0,  0],
            [0,  0,  0,  1,  1,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0]
        ],
            # a board that is one move away from winning for p2
            [
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  1,  0,  0],
            [0,  0,  0, -1, -1,  0,  0,  0],
            [0,  0,  0, -1, -1,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0]
        ],
            # one move will lead to losing
            [
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0, -1, -1,  0,  0,  0],
            [0,  0,  0, -1,  1,  0,  0,  0],
            [0,  0,  0,  0, -1,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0],
            [0,  0,  0,  0,  0,  0,  0,  0]

        ]]

    # ensure bots will always take an obvious winning move
        tree = GameTree(boards[0], 1)
        (row, col) = tree.get_best_move()
        #tree.print_target_depth(1)
        #tree.print_target_depth(2)
        self.assertEqual((row, col), (1, 3))

        
        

        tree = GameTree(boards[1], -1)
        (row, col) = tree.get_best_move()
        #print(row, col)
        self.assertEqual((row, col), (1, 6))

    # ensure bots will always avoid obvious losing moves
        tree = GameTree(boards[2], 1)
        (row, col) = tree.get_best_move()
        #tree.print_target_depth(1)
        #tree.print_target_depth(2)
        self.assertNotEqual((row, col), (2, 4))
        self.assertNotEqual((row, col), (6, 4))

        # export_csv.set_arr(boards)
        # export_csv.export()


if __name__ == '__main__':
    unittest.main()
