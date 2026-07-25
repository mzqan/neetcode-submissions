class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # at a given square, you must come from a square bove or to the left
        # tabluation: we remember the values for the above row and the current row
        #             we can pull above and left (if j != 0)
    
        ROWS, COLS = m, n
        aboveRow = [0] * COLS
        aboveRow[0] = 1 # starting position

        for i in range(ROWS):
            currRow = [1] * COLS
            for j in range(COLS):
                left = currRow[j-1] if j else 0
                above = aboveRow[j]
                currRow[j] = above + left
            aboveRow = currRow

        return aboveRow[-1]