import unittest

import main as sol

class MatrixTest(unittest.TestCase):

    def test(self):
        mat = [[0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(mat, sol.matrix())

unittest.main()
