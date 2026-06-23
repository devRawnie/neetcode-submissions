class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            print(l, r )
            m = l + (r-l)//2
            if nums[m] == target:
                return m
            
            if target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1