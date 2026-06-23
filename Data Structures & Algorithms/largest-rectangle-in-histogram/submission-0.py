class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        res = 0
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                curr = stack.pop()
                l = stack[-1] if stack else -1
                res = max(res, heights[curr]*(i-l-1))

            stack.append(i)

        while stack:
            top = stack.pop()
            l = stack[-1] if stack else -1
            res = max(res, heights[top]*(n-l-1))

        return res
