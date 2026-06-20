class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        list = []
        intervals.sort()
        list.append(intervals[0])
        for i in intervals[1:]:
            if list[-1][1] >= i[0]:
                list[-1][1] = max(i[1],list[-1][1])
            else:
                list.append(i)
        return list


        