class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force: try every idx as a possible start
        # greedy: loop through each idx, if going ot the NEXT would be negative, consider that as NEW start

        # 5 0 3 10 1 
        # 1 7 3  7 0

        # impossible because insufficient gas
        if sum(gas) < sum(cost):
            return -1
        
        startIdx = 0
        currTank = 0

        for i in range(len(gas)):
            currTank = currTank + gas[i] - cost[i]

            # invalid, consider new start idx and rest 
            if currTank < 0:
                startIdx = i + 1
                currTank = 0

        return startIdx

