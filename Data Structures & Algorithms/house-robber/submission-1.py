class Solution:
    def rob(self, nums: List[int]) -> int:
        stolen = [n for n in nums]

        # at a given idx i, 
        #   either come from i - 2  or  i -3

        for i, n in enumerate(nums):
            idx = -1
            if i > 1:
                idx = i - 2
                if i > 2 and stolen[i-3] > stolen[i-2]:
                    idx = i - 3
            if idx != -1:
                stolen[i] += stolen[idx]
            
        return max(stolen)
    
        