class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # at each idx , we know the length of longest strictly increasing
        # for i from start -> end
        #   for j from start -> i
        #   check if num[j] < num[i] and update dp[i] for max 
        res = (0, float('-inf'))
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and (dp[j] + 1) > dp[i]:
                    dp[i] = dp[j] + 1

        return max(dp)