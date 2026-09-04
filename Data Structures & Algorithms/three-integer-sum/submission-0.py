class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the numbers
        nums.sort() #inplace
        output_list = []
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:  #Duplicate
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[left] + nums[right] + num
                if total > 0:
                    right-=1
                elif total < 0:
                    left+=1
                else:
                    output_list.append([nums[left], nums[right], num])
                    left+=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
            
        return output_list
            
            
        

        