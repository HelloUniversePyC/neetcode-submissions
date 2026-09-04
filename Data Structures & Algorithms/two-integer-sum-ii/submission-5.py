class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        solution = []
        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                right-=1
            elif total < target:
                left+=1
            else:
                solution = [left+1, right+1]
                left+=1
        return solution

        


        