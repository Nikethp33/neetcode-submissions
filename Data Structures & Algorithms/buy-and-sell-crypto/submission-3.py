class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_price = prices[0]
        profit = 0

        for price in prices:
            b_price = min(b_price, price)
            profit = max(profit, price - b_price)

        return profit
