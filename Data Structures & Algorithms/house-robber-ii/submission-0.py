class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
    
        def robLinear(houses):
            # max robbed up until 2 house ago (gap of 1)
            # aka we can take the current
            rob1 = 0
            # max robbed up until prev house (gap of 0)
            # aka we must skip the current
            rob2 = 0

            # at each idx i,
            #   choose to use h + rob1 or rob2 (dont take this one)
            # advance rob1 and rob2 by 1
            for h in houses:
                # include curr, or skip curr for max robbed up till this h
                newRob = max(rob1 + h, rob2)
                # advance robs 
                rob1 = rob2
                rob2 = newRob
        
            # return last value, max rob
            return rob2

        # from 0 -> n-1
        skip_last = robLinear(nums[:-1])
        # from 1 -> n
        skip_first = robLinear(nums[1:])

        return max(skip_last, skip_first)
