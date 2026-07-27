"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        mp = defaultdict(int)
        # starts = need room, end = free room
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev = 0
        res = 0
        # gets concurrent at given timestamp
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res