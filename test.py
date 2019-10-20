import unittest

import main as sol

class MatrixTest(unittest.TestCase):
    def test(self):
        mat = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(mat, sol.matrix())

class CheckRowsTest(unittest.TestCase):
	def test_0_token(self):
		mat = sol.matrix()
		self.assertEqual(False, sol.check_rows(mat, 1))
		self.assertEqual(False, sol.check_rows(mat, 2))
	
	def test_3_tokens(self):
		mat = sol.matrix()
		mat[5][0] = 1
		mat[5][1] = 1
		mat[5][2] = 1
		self.assertEqual(False, sol.check_rows(mat, 1))
		mat[5][0] = 2
		mat[5][1] = 2
		mat[5][2] = 2
		self.assertEqual(False, sol.check_rows(mat, 2))
	
	def test_4_tokens(self):
		mat = sol.matrix()
		mat[5][0] = 1
		mat[5][1] = 1
		mat[5][2] = 1
		mat[5][3] = 1
		self.assertEqual(True, sol.check_rows(mat, 1))
		mat[5][0] = 2
		mat[5][1] = 2
		mat[5][2] = 2
		mat[5][3] = 2
		self.assertEqual(True, sol.check_rows(mat, 2))

class CheckColumnsTest(unittest.TestCase):
	def test_0_token(self):
		mat = sol.matrix()
		self.assertEqual(False, sol.check_columns(mat, 1))
		self.assertEqual(False, sol.check_columns(mat, 2))
	
	def test_4_tokens(self):
		mat = sol.matrix()
		mat[5][0] = 1
		mat[4][0] = 1
		mat[3][0] = 1
		mat[2][0] = 1
		self.assertEqual(True, sol.check_columns(mat, 1))
		mat[3][5] = 2
		mat[2][5] = 2
		mat[1][5] = 2
		mat[0][5] = 2
		self.assertEqual(True, sol.check_columns(mat, 2))

class CheckDiagTest(unittest.TestCase):
	def test_0_token(self):
		mat = sol.matrix()
		self.assertEqual(False, sol.check_diag(mat, 1))
		self.assertEqual(False, sol.check_diag(mat, 2))
	
	def test_4_tokens(self):
		mat = sol.matrix()
		mat[5][0] = 1
		mat[4][1] = 1
		mat[3][2] = 1
		mat[2][3] = 1
		self.assertEqual(True, sol.check_diag(mat, 1))
		mat[5][0] = 2
		mat[4][1] = 2
		mat[3][2] = 2
		mat[2][3] = 2
		self.assertEqual(True, sol.check_diag(mat, 2))

unittest.main()
