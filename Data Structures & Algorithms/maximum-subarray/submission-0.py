class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # at each idx, we can choose either to include it to curr OR start a new
        #              choose the maximum, update best res seen
        
        res = float('-inf')
        curr = 0

        for n in nums:
            # include to curr subarray
            keep = curr + n

            # better to keep or start new
            curr = max(keep, n)

            # update res
            res = max(res, curr)
        
        return res
            