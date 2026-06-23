class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        res = 0
        m = {}
        i = 0
        for j in range(n):
            if s[j] in m:
                i = max(m[s[j]] + 1, i)

            m[s[j]] = j
            res = max(res, j-i+1)
        return res


