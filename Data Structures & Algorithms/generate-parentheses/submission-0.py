class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []
        def bt(o, c):
            if o == c == n:
                result.append("".join(stack))
                return

            if o < n:
                stack.append("(")
                bt(o+1, c)
                stack.pop()
            if c < o:
                stack.append(")")
                bt(o, c+1)
                stack.pop()
        bt(0,0)
        return result