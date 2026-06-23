class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_arr = nums.copy()
        right_arr = nums.copy()
        for i in range(1, n):
            left_arr[i] *= left_arr[i-1]

        for i in range(n-2, -1, -1):
            right_arr[i] *= right_arr[i+1]

        for i in range(n):
            left_val = 1
            right_val = 1
            if i > 0:
                left_val = left_arr[i-1]

            if i < n-1:
                right_val = right_arr[i+1]

            nums[i] = left_val * right_val

        return nums