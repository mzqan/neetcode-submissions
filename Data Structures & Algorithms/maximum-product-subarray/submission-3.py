class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i], for each idx we know the max/min product subarray INCLUDING that point
        # this makes sure we catch - * - = +
        dpMax = [n for n in nums]
        dpMin = [n for n in nums]

        for i in range(1, len(nums)):
            options = (nums[i], nums[i] * dpMax[i-1], nums[i] * dpMin[i-1])

            dpMin[i] = min(options)
            dpMax[i] = max(options)

        return max(dpMax)
