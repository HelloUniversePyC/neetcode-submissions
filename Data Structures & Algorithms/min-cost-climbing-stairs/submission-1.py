class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def price(idx):
            if idx == 0 or idx ==1:
                return 0
            if idx in memo:
                return memo[idx]
            left = price(idx-1) + cost[idx-1]
            right = price(idx-2)+ cost[idx-2]
            memo[idx] = min(left, right)
            return memo[idx]
        return price(len(cost))
        