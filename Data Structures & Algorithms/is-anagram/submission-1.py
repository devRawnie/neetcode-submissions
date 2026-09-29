class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = [0 for _ in range(26)]
        for c in s:
            mp[ord(c)-ord('a')]+= 1

        for c in t:
            if mp[ord(c)-ord('a')] == 0:
                return False
            mp[ord(c)-ord('a')] -= 1

        return not any(x > 0 for x in mp)