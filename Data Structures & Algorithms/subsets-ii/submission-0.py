class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        def dfs(i, cur):
            if i >= len(nums):
                result.append(cur.copy())
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()

            while i < len(nums) - 1 and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1, cur)
        dfs(0, [])
        return result