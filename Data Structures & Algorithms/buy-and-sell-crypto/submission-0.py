class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        for sell in range(len(prices)):
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            else:
                #Found a new lower price shift
                buy = sell
        return max_profit
            
           

            

