class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for i,sell in enumerate(prices):
            if sell < prices[buy]:
                buy = i
            else:
                curr_profit = sell - prices[buy]
                max_profit = max(curr_profit, max_profit)
        return max_profit

        