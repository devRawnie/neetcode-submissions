class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculate(number, power):
            if number == 0:
                return 0
            if power == 0:
                return 1

            if power % 2 == 1:
                return number * calculate(number, power - 1)

            return calculate(number * number, power // 2)


        result = calculate(number=x, power=abs(n))
        if n > 0:
            return result
        
        return (1 / result)
