class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # at each idx, 
        #   if sum is odd then NO
        #   
        # BRUTE FORCE:
        #   (optimization) sum is odd then NO
        #   backtrack and generate all different splits 2^n

        # question: can we pick a subset whose sum is totalSum / 2
        # at each idx, we either take current number into subset or skip 
        # keep reducing target (sum / 2) 
        # base case: target becomes 0 (success) 
        # base case: run out of numbers/target is negative (failure)

        totalSum = sum(nums)
        n = len(nums)

        if totalSum % 2:
            return False

        target = totalSum // 2
        memo = [[-1] * (target + 1) for _ in range(n + 1)]


        def dfs(i, target):
            if i >= n:
                return target == 0

            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = (dfs(i+1, target) or dfs(i+1, target-nums[i]))

            return memo[i][target]
        
        return dfs(0, target)
