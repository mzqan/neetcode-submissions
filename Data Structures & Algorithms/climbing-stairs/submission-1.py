class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * n

        # bottom up:
        # for each step i, add number of ways to get from i - 1 (1 step) and i - 2 (2 steps)
        for i in range (0, n):
            if i == 0:
                # 1
                ways[i] = 1
                continue
            elif i == 1:
                # 1, or 1 + 1
                ways[i] = 2
            else: 
                ways[i] = ways[i-1] + ways[i-2]
    
        return ways[-1]

