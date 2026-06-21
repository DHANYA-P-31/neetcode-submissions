class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0][1]
        count = 0
        for i in intervals[1:]:
            if i[0]<prev:
                prev = min(prev,i[1])
                count += 1
            else:
                prev = max(prev,i[1])
        return count
