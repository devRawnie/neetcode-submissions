class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        part = []

        def isPalindrome(p):
            pn = len(p)
            for i in range(pn//2):
                if p[i] != p[pn-i-1]:
                    return False

            return True

        def dfs(i):
            if i == len(s):
                result.append(part.copy())
                return

            for pos in range(i, len(s)):
                if isPalindrome(s[i:pos+1]):
                    part.append(s[i:pos+1])
                    dfs(pos+1)
                    part.pop()

        dfs(0)
        return result

