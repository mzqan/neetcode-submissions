class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # recursion: call dfs(0, target) for final soln
        #   dfs (i, amt) represents the # of ways to get amt using nums[i:]
        #   base case: amt == 0 and i == len(nums) -> 1 way aka dont pick, else i >= len(nums) -> 0 ways aka no options
        #   at each call, we memoize the sum of adding/subtracting each n in nums

        memo = {}

        def dfs(i, amt):
            # finished all numbers and valid
            if amt == 0 and i == len(nums):
                return 1

            # no more numbers to check and invalid
            if i >= len(nums):
                return 0

            if (i,amt) in memo:
                return memo[(i, amt)]

            # total ways = add path + subtract path
            memo[(i, amt)] = dfs(i + 1, amt + nums[i]) + dfs(i + 1, amt - nums[i])
            
            return memo[(i,amt)]
        
        return dfs(0, target)

            