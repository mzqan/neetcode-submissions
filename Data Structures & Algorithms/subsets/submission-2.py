class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, i, path):
            nonlocal res
            curr = path.copy()

            if i == len(nums):
                res.append(curr)
                return

            # exclude
            backtrack(nums, i+1, curr)

            # include
            curr.append(nums[i])
            backtrack(nums, i+1, curr)
            
        backtrack(nums, 0, [])
        return res