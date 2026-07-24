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

        def dfs(i, target):
            if i >= n:
                return target == 0

            if target < 0:
                return False

            return dfs(i + 1, target - nums[i]) or dfs(i + 1, target)
        
        return dfs(0, target)
