class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort intervals by start time
        #  
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # if not overlapping, update end
            if start >= prevEnd:
                prevEnd = end
            # if overlapping, keep the one that ends earlier (greedy)
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res