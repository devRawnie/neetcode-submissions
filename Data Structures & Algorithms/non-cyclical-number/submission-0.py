class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def get_digit_sum(num):
            res = 0
            while num > 0:
                d = num % 10
                res += d**2
                num //= 10

            return res

        while n != 1:
            nxt = get_digit_sum(num=n)
            if nxt in seen:
                return False
            seen.add(nxt)
            n = nxt

        return True
