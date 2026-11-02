class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, cur = [], []
        def dfs(i):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i == len(nums):
                return
            if sum(cur) >= target:
                return
            cur.append(nums[i])
            dfs(i)
            cur.pop()
            dfs(i+1)
        dfs(0)
        return res

        