"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort by start time
        # compare current idx start to prev idx end
        prev = -1
        for i in sorted(intervals, key = lambda x : x.start):
            if prev > i.start:
                return False
            prev = i.end
        
        return True