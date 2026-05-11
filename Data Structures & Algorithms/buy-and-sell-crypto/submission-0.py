class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = i+1

        while i < len(prices) - 1 and j < len(prices):
            profit = max(profit, prices[j]-prices[i])
            if prices[j] > prices[i]:
                j += 1

            else:
                profit = max(profit, prices[j-1]-prices[i])
                i = j
                j = i + 1

        return profit