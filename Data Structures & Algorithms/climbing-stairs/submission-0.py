class Solution:
    cache = dict()
    def climbStairs(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n == 0 or n == 1:
            return 1
        left = self.climbStairs(n-2)
        right = self.climbStairs(n-1)
        self.cache[n] = left+ right
        return self.cache[n]
        