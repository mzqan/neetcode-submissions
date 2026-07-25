class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each idx, we can choose either to include it to curr OR start a new
        #              choose the maximum, update best res seen
        
        res = float('-inf')
        curr = 0 # dp[i]
 
        for n in nums:
            # include to curr subarray
            keep = curr + n # dp[i-1] + nums[i]

            # better to keep or start new
            curr = max(keep, n)

            # update res
            res = max(res, curr)
        
        return res
            