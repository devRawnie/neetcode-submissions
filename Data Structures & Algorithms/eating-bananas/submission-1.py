class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def check(x):
            return sum([math.ceil(i/x) for i in piles])

        while l < r:
            m = l + (r-l)//2
            if check(m) <= h:
                r = m
            else:
                l = m+1

        return l
        