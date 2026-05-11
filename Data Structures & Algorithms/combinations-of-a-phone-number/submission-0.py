class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        stack = []
        def bt(di):
            if di == len(digits):
                result.append("".join(stack))
                return

            for ci in charMap[digits[di]]:
                stack.append(ci)
                bt(di+1)
                stack.pop()

        bt(0)
        return result
