class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # maintain variable caled goal, which is the leftmost index we must be able to rech
        #   initialized to last index
        # work backwards, if from index i can jump to/past (since nums[i] is MAX distance) current goal, then index i becomes new goal

        goal = len(nums) - 1
        
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
                
        return goal == 0 