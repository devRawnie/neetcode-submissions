class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def overlap(a, b):
            if a[0] >= b[0] and a[0] <= b[1]:
                return True
            if a[1] >= b[0] and a[0] <= b[1]:
                return True

            return False

        intervals.sort(key=lambda x: x[0])
        result = []
        for i in intervals:
            if not result:
                result.append(i)
            elif overlap(result[-1], i) or overlap(i, result[-1]):
                    result[-1][0] = min(result[-1][0], i[0])
                    result[-1][1] = max(result[-1][1], i[1])
            else:
                result.append(i)

        return result