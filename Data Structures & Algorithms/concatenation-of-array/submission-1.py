class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        sz = len(nums)
        new_arr = [0] * (sz * 2)

        for i in range(sz):
            new_arr[i] = nums[i]
            new_arr[i+sz] = nums[i]

        return new_arr