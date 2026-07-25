class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # at a given square, you must come from a square bove or to the left
        # tabluation: save # ways you can reach (i,j) square in a m x n table
        # start with the top row go left to right
        # at given (i,j), check i-1 for left (unless i == 0) and j - 1 for above (unless j == 0)

        ROWS, COLS = m, n
        dp = [[0] * COLS for _ in range(ROWS)]
        dp[0][0] = 1

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j ==0:
                    continue
                left = dp[i][j-1] if j else 0
                above = dp[i-1][j] if i else 0
                dp[i][j] = above + left

        return dp[ROWS-1][COLS-1]