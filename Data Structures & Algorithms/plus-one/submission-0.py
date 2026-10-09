class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        rem = 1
        for d in digits[::-1]:
            nd = d + rem
            result.append(nd%10)
            rem = nd // 10

        if rem:
            result.append(rem)

        return result[::-1]