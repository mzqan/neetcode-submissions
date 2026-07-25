class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # at each idx, either jump or not
        # recursion: dfs(i) if you can make it to end from nums[i:]
        #   memoize, memo[i] = jump path or skip path
        #   base case: i == n - 1 -> valid, nums[i] == 0 or i > n -> invalid
        
        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums) - 1:
                return True
            
            
            for j in range(nums[i], 0, -1):
                if dfs(i+j):
                    memo[i] = True
                    return True
                
            memo[i] = False
            return memo[i]
            
        return dfs(0)