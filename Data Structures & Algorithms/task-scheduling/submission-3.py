class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = 0
        count = Counter(tasks)
        maxh = [-c for c in count.values()]
        heapq.heapify(maxh)
        q = deque()
        while maxh or q:
            t += 1
            if maxh:
                task = 1 + heapq.heappop(maxh)
                if task:
                    q.append([task, t+n])
            
            if q and q[0][1] == t:
                heapq.heappush(maxh, q.popleft()[0])

        return t        
