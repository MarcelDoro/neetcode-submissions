class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def are_overlapping(first_interval: List[int], second_interval: List[int]) -> bool:
            if (first_interval[1] < second_interval[0] or
                first_interval[0] > second_interval[1]):
                return False

            return True


        res = []
        inserted_newInterval = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif are_overlapping(interval, newInterval):
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            elif interval[0] > newInterval[1]:
                if not inserted_newInterval:
                    res.append(newInterval)
                    inserted_newInterval = True
                res.append(interval)


        if not inserted_newInterval:
            res.append(newInterval)
            inserted_newInterval = True
            
        return res
