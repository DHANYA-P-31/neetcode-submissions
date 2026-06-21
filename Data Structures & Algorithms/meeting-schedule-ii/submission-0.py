"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        n = len(intervals)
        h = []
        for i in range(n):
            if h and h[0]<= intervals[i].start:
                heapq.heappop(h)
            heapq.heappush(h,intervals[i].end)
        return len(h)