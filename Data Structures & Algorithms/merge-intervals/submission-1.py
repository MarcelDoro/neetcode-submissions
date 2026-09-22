class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(first: List[int], second: List[int]) -> bool:
            if first[1] < second[0] or first[0] > second[1]:
                return False

            return True

        intervals.sort(key= lambda x: x[0])
        res = []
        i = 0
        while i < len(intervals):
            new_interval = intervals[i]
            while i + 1 < len(intervals) and overlap(new_interval, intervals[i + 1]):
                new_interval[0] = min(new_interval[0], intervals[i + 1][0])
                new_interval[1] = max(new_interval[1], intervals[i + 1][1])
                i += 1
            
            res.append(new_interval)
            i += 1

        return res
