class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i = 0
        j = len(heights)-1
        while i < j:
            curr_result = abs(i-j) * min(heights[i], heights[j])
            ans = max(curr_result, ans)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return ans