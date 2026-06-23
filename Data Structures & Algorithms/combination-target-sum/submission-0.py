class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, subs, n):
            if i >= len(nums):
                return

            if n < 0:
                return

            if n == 0:
                result.append(subs.copy())
                return

            subs.append(nums[i])
            dfs(i, subs, n-nums[i])
            subs.pop()
            dfs(i+1, subs, n)


                
        dfs(0, [], target)
        return result