class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # at a given point = 1, go up right down left unless already visited, then 
        # base case: if already visited / a 0 return

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # out of bounds or water
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == '0':
                return

            # mark as "visited" / already accounted for as an island
            grid[r][c] = "0"

            dfs(r-1, c) # up
            dfs(r+1, c) # down
            dfs(r, c-1) # left
            dfs(r, c+1) # right


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                        dfs(r, c)
                        islands += 1
        
        return islands
