class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = ["+","-","*","/"]
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                a = stack.pop()
                b = stack.pop()
                val = eval(f"int({b}{t}{a})")
                stack.append(val)

        return stack[-1]