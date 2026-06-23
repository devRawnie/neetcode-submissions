class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        ans = 0
        for n in values:
            t = n
            t_ans = 1
            if t-1  not in values:
                while t+1 in values:
                    t+=1
                    t_ans += 1

            ans = max(ans, t_ans)

        return ans


