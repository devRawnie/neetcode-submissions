class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        3, 4, 5, 6, 1, 2
                 l  r  
        5, 6, 1, 2, 3, 4
           l  r        
        1, 2, 3, 4, 5, 6
        l     m        r

        l < m
        r < m
        shift left

        l > m
        r > m
        shift right


        l < m
        r > m
        """

        l = 0
        r = len(nums) - 1
        while r-l > 1:
            m = l + (r-l)//2
            if nums[l] < nums[m] < nums[r]:
                return nums[l]

            if nums[l] < nums[m] and nums[r] < nums[m]:
                l = m
            elif nums[l] > nums[m] and nums[r] > nums[m]:
                r = m

        return min(nums[l], nums[r])

        
        