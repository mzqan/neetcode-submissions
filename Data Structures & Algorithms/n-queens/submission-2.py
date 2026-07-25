class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # HINT: row-by-row assignment
        # at each row (i from 0 -> n - 1), we check if col and diagonals are valid
        # curr = [""] for _ in range(n)
        # res = []
        # recursion: dfs(r) for evaluating current row r ()
        #   iterate through each c, and place queen if valid
        #   base case: r > n, add curr copy to res

        res = []
        curr = [["."] * n for _ in range(n)]

        cols = set()  # c
        lDiag = set() # r - c
        rDiag = set() # r + c

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in curr])
                return
            
            # implicitly handles include/exclude
            for c in range(n):
                # placement is valid
                if not (c in cols or r-c in lDiag or r+c in rDiag):
                    curr[r][c] = "Q"
                    cols.add(c)
                    lDiag.add(r-c)
                    rDiag.add(r+c)
                    backtrack(r+1)
                    curr[r][c] = "."
                    cols.remove(c)
                    lDiag.remove(r-c)
                    rDiag.remove(r+c)
            
        backtrack(0)
        return res



