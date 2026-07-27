class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_price = 999999
        s_price = 0
        profit = 0

        for i in range(len(prices)):
            if prices[i] < b_price:
                b_price = prices[i]
                s_price = 0
                
            else:
                s_price=max(s_price,prices[i])
                profit = max((s_price-b_price),profit)
        return profit
