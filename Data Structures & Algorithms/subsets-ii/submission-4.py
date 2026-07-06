class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        nums.sort()
        # backtrack
        # sort to systematically address 
        # track at which idx we left off at
        # loop thru rest of nums from idx, end
        # choose to include or exclude
        # to handle duplicate subsets, if prev was the same we skip
        # becaues it would've already been handled by the previous's exclude case
        # base case is if i == len(nums)

        def backtrack(i):
            res.append(curr.copy())

            for j in range(i, len(nums)):
                # not the first, and its same as previous
                if j > i and nums[j] == nums[j-1]:
                    continue

                # include
                curr.append(nums[j])
                backtrack(j+1)

                #exclude
                curr.pop()

        backtrack(0)

        return res