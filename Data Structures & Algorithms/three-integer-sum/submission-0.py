class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        n = len(nums)
        for i in range(n-2):
            target = -1 * nums[i]
            l = i+1
            r = n-1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

                elif curr > target:
                    r -= 1
                else:
                    l += 1

        return list(result)
