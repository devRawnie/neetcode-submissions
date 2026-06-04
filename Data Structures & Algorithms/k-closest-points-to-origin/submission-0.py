class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_distance = []

        for x,y in points:
            d = x**2 + y**2
            points_distance.append((d, x, y))

        heapq.heapify(points_distance)
        result = []
        while k > 0:
            d, x, y = heapq.heappop(points_distance)
            result.append([x,y])
            k -= 1


        return result