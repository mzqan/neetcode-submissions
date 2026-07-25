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
        curr = [""] * n

        def isValid(r, c):
            # check all rows above
            for i in range(r):
                # queen in same col
                if curr[i][c] == "Q":
                    return False

                # queen in left or right diag
                offset = r - i
                if c - offset >= 0 and curr[i][c - offset] == "Q":
                    return False
                
                if c + offset < n and  curr[i][c + offset] == "Q":
                    return False
            
            return True

        def backtrack(r):
            if r == n:
                res.append(curr.copy())
                return
            
            # implicitly handles include/exclude
            for c in range(n):
                # col is valid
                if isValid(r, c):
                    curr[r] += "." * c
                    curr[r] += "Q"
                    curr[r] += "." * (n - c - 1)
                    backtrack(r+1)
                    curr[r] = ""
            
        backtrack(0)
        return res



