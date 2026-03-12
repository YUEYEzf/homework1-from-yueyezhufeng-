import unittest
from src.eight_queens import EightQueens

class TestEightQueens(unittest.TestCase):
    def test_n4_solution_count(self):
        """验证 4 皇后问题有 2 个解"""
        eq = EightQueens(4)
        self.assertEqual(len(eq.solve()), 2)

    def test_n8_solution_count(self):
        """验证 8 皇后问题有 92 个解"""
        eq = EightQueens(8)
        self.assertEqual(len(eq.solve()), 92)

    def test_solution_validity(self):
        """验证解的合法性：无同列、同斜线皇后"""
        eq = EightQueens(8)
        sol = eq.solve()[0]
        for i in range(8):
            for j in range(i + 1, 8):
                self.assertNotEqual(sol[i], sol[j], "存在同列皇后")
                self.assertNotEqual(abs(i - j), abs(sol[i] - sol[j]), "存在同斜线皇后")

if __name__ == '__main__':
    unittest.main()