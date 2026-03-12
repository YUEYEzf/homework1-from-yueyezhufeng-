class EightQueens:
    def __init__(self, n=8):
        self.n = n
        self.solutions = []
        self.board = [-1] * n  # board[row] = column

    def is_safe(self, row, col):
        """检查在 (row, col) 放置皇后是否安全"""
        for i in range(row):
            if self.board[i] == col or abs(row - i) == abs(col - self.board[i]):
                return False
        return True

    def backtrack(self, row=0):
        """回溯法递归放置皇后"""
        if row == self.n:
            self.solutions.append(self.board.copy())
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.backtrack(row + 1)
                self.board[row] = -1  # 回溯

    def solve(self):
        """启动求解，返回所有解"""
        self.backtrack()
        return self.solutions

    def print_solution(self, solution):
        """打印单个解的棋盘"""
        for row in range(self.n):
            line = ['.'] * self.n
            line[solution[row]] = 'Q'
            print(' '.join(line))

if __name__ == "__main__":
    # 测试 4 皇后
    eq4 = EightQueens(4)
    print(f"4 皇后解数: {len(eq4.solve())}")
    # 测试 8 皇后
    eq8 = EightQueens(8)
    print(f"8 皇后解数: {len(eq8.solve())}")