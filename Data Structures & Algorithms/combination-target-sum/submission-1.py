class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtrack(i, currSum):
            if currSum == target:
                res.append(curr.copy())
                return
            
            for j in range(i, len(nums)):
                # include
                if (currSum + nums[j]) <= target:
                    curr.append(nums[j])
                    backtrack(j, currSum + nums[j])
                    curr.pop()

        backtrack(0, 0)

        return res