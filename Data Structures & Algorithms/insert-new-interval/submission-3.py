class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iterate through until curr start is after new 
        # if start or end is found within curr interval, take the min(start) and max(end) -> update "newInterval"
        #    keep stepping forward until end is BEFORE next, then we can add it to our result.. 
        if not intervals:
            return [newInterval]

        i = 0
        n = len(intervals)
        res = []

        # curr end < new start
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
 
        # new is in next interval
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n:
            res.append(intervals[i]) 
            i += 1

        return res