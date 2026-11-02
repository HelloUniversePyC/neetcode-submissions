class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)-1
        farthest_reach = 0
        for i,num in enumerate(nums):
             curr_reach = i + num
             if i > farthest_reach:
                 return False
             farthest_reach = max(curr_reach, farthest_reach)
             if farthest_reach >= target:
                return True
        return farthest_reach >= target

