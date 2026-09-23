class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0
        i = 0
        while i + 1 < len(intervals):
            first = intervals[i]
            second = intervals[i + 1]
            if second[0] < first[1]:
                res += 1
                if first[1] < second[1]:
                    del intervals[i + 1]
                else:
                    del intervals[i]
            else:
                i += 1

        return res