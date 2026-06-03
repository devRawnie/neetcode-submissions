class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2:
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)
            print(f's1: {s1}, s2: {s2}')
            if s1 < s2:
                heapq.heappush(stones, -1 * (s2-s1))
            elif s2 < s1:
                heapq.heappush(stones, -1 * (s1-s2))

        if len(stones) == 1:
            return -1 * stones[0]
        
        return 0
        
            
