class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {} 
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        rev_counter = []
        for key, val in counter.items():
            rev_counter.append([-val, key])

        heapq.heapify(rev_counter)
        q = []
        time = 0
        while q or rev_counter:            
            if rev_counter:
                num, task = heapq.heappop(rev_counter)                
                if -num > 1:
                    q.append([time + n, num + 1, task])
            if q and q[0][0] == time:
                _, num, task = q.pop(0)
                heapq.heappush(rev_counter, [num, task])
            time += 1

        return time