class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = dict()
        solution = []
        for i,num in enumerate(nums):
            complement = target - num
            if complement in diff_dict:
                solution = [diff_dict[complement], i]
                break
            diff_dict[num] = i
        return solution
        