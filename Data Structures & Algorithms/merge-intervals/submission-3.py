class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        # iterate left to right
        # if res end time overlaps (after current start), then update res' end time
        
        res = []
        for interval in sorted(intervals):
            # overlaps with prev added
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        
        return res