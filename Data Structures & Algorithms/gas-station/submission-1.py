class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force: try every idx as a possible start
        # greedy: loop through each idx, 
        #   if going to next would cause negative tank, all indexes up to this point are INVALID (even with a "headstart" from failed idx it still ran out)


        # impossible because insufficient gas
        if sum(gas) < sum(cost):
            return -1
        
        startIdx = 0
        currTank = 0

        for i in range(len(gas)):
            currTank = currTank + gas[i] - cost[i]

            # invalid, consider NEXT station as new start idx and reset tank
            if currTank < 0:
                startIdx = i + 1
                currTank = 0

        return startIdx

