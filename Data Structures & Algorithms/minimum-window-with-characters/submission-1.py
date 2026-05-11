class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        def compare_dict(d1, d2):
            for k, v in d1.items():
                if v > d2.get(k, 0):
                    return False
            return True

        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        source = {}
        l = 0
        r = 0
        ans = ""
        while r < len(s):
            while compare_dict(target, source):
                substr = s[l:r]
                if not ans or len(substr) < len(ans):
                    ans = substr

                source[s[l]] = max(0, source[s[l]] - 1)
                l += 1

            source[s[r]] = source.get(s[r], 0) + 1
            r += 1


        while compare_dict(target, source):
            substr = s[l:r+1]
            if not ans or len(substr) < len(ans):
                ans = substr
            source[s[l]] = max(0, source[s[l]] - 1)
            l += 1

        return ans            




