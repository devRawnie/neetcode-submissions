class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        i = 0
        max_so_far = 10e5
        for j in range(len(nums)):
            heapq.heappush(heap, (-1 * nums[j], j))
            if j >= k-1:
                while heap[0][1] <= j - k:
                    heapq.heappop(heap)

                ans.append(-1 * heap[0][0])


        return ans
