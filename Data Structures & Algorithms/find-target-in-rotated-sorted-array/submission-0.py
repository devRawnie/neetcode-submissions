class Solution:
    def find_pivot(self, nums):
        l = 0
        r = len(nums) - 1
        while r-l > 1:
            m = l + (r-l)//2
            if nums[l] < nums[m] < nums[r]:
                return l

            if nums[l] < nums[m] and nums[r] < nums[m]:
                l = m
            elif nums[l] > nums[m] and nums[r] > nums[m]:
                r = m

        return l if nums[l] < nums[r] else r

    def bin_search(self, nums, start, end, target):
        n = len(nums)
        while start < end:
            mid = start + (end-start)//2
            if nums[mid] == target:
                return mid
    
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid + 1

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pivot = self.find_pivot(nums)
        if target >= nums[pivot] and target <= nums[-1]:
            return self.bin_search(nums, pivot, n-1, target)

        else:
            return self.bin_search(nums, 0, pivot, target)

        return -1