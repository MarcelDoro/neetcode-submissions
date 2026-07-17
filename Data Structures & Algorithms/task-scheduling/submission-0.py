class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        
        for task in tasks:
            counter[task] = counter.get(task, 0) + 1

        reversed_counter = []
        for key, val in counter.items():
            reversed_counter.append([-val, key])

        heapq.heapify(reversed_counter)
        q = []
        time = 0
        while q or reversed_counter:
            print("rev: ", reversed_counter)
            print("q: ", q)
            if reversed_counter:
                num, task = heapq.heappop(reversed_counter)
                num = -num
                if num > 1:
                    q.append([time + n, num - 1, task])
            if q and q[0][0] == time:
                _, num, task = q.pop(0)
                heapq.heappush(reversed_counter, [-num, task])
            time += 1

        return time