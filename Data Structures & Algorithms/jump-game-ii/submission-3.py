class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        l = r = 0

        # stop once we've reached end
        while r < len(nums) - 1:
            farthest = 0

            # get NEXT farthest reachable from this search range
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # update left to end of search range of previous step
            l = r + 1

            # update all-time/NEXT farthest reachable
            r = farthest

            # we've taken one step, after advancing form prev farthest
            steps += 1
        return steps