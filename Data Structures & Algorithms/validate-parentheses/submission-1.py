class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        mp = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in mp:
                stack.append(c)

            else:
                if len(stack) == 0:
                    return False

                t = stack.pop()
                if mp[t] != c:
                    return False

        return len(stack) == 0