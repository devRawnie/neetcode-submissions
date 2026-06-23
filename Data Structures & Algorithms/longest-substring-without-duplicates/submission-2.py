class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        res = 0
        m = {}
        i = 0
        j = i+1
        m[s[i]] = i
        while j < n:
            if s[j] in m:
                i = max(m[s[j]] + 1, i)

            m[s[j]] = j
            res = max(res, j - i+1)
            j += 1

        res = max(res, j - i)
        return res


