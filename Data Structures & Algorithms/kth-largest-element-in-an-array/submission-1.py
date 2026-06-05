class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)
        while k > 1:
            p = heapq.heappop(nums)
            k -= 1

        return -1 * nums[0]