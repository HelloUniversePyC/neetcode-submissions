class Solution:
    
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        def max_money(i):
            if i >= len(nums):
                return 0
            if i in self.memo:
                return self.memo[i]
            self.memo[i] = max(max_money(i+1), nums[i] + max_money(i+2))
            return self.memo[i]
        return max_money(0)
        