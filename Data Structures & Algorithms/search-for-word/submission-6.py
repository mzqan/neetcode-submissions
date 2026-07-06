class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # from each cell
        # 4 choices, up left right down
        # track current word
        # track which indices we've already visited
        # base case, visited > word size then return or check

        visited = set()

        ROWS, COLS = len(board), len(board[0])
        
        def backtrack(r, c, i):
            if i == len(word):
                return True

            if not (-1 < r < ROWS and -1 < c < COLS):
                return False

            if (r,c) in visited or board[r][c] != word[i]:
                return False
            
            visited.add((r,c))

            if backtrack(r-1,c,i+1) or backtrack(r,c-1,i+1) or backtrack(r+1,c,i+1) or  backtrack(r,c+1,i+1):
                return True
            
            visited.remove((r,c))

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True
            
        return False