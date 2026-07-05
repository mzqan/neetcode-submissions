class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        used = set()

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for j in range(len(nums)):
                if j not in used:
                    used.add(j)
                    curr.append(nums[j])

                    backtrack()

                    used.remove(j)
                    curr.pop()
            

        backtrack()

        return res

