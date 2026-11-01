class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        def least_coins(remain):
            if remain == 0:
                return 0
            if remain < 0:
                return float('inf')
            
            min_coins = float('inf')
            for coin in coins:
                result = least_coins(remain - coin) if not (remain-coin) in self.memo else self.memo[remain-coin]
                self.memo[remain-coin] = result
                if result != float('inf'):
                    min_coins = min(min_coins, result+1)
            return min_coins 
        minimum = least_coins(amount)
        return minimum if minimum != float('inf') else -1

                

                

        