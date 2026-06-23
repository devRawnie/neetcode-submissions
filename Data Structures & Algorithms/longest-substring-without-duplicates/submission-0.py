class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return n

        res = 0
        m = set()
        i = 0
        j = i+1
        m.add(s[i])
        while j < n:
            print(m)
            if s[j] not in m:
                m.add(s[j])
                j += 1
            else:
                res = max(res, j - i)
                m.remove(s[i])
                i += 1

        res = max(res, j - i)
        return res


