class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_unique = set(nums)
        max_run = 0
        for i,num in enumerate(nums):
            if not (num-1) in nums_unique:
                curr_run = 1
                start = num
                while True:
                    if (start+1) in nums_unique:
                        curr_run+=1
                        start+=1
                    else:
                        break
                max_run = max(curr_run, max_run)
        return max_run

                
        