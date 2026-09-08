class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for n in range(len(prices)):
            for i in range(n+1, len(prices)):
                diff = prices[i] - prices[n]
                if diff > profit:
                    profit = diff
        return profit

