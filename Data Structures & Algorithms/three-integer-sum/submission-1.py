class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the numbers
        nums.sort() #inplace
        output_list = []
        for i,first in enumerate(nums):
            if i > 0 and first == nums[i-1]:  #Duplicate
                continue
            second = i+1
            third = len(nums)-1
            while second < third:
                total = first + nums[second] + nums[third]
                if total > 0:
                    third-=1
                elif total < 0:
                    second+=1
                else:
                    output_list.append([nums[second], nums[third], first])
                    second+=1
                    while nums[second] == nums[second-1] and second < third:
                        second+=1
            
        return output_list
            
            
        

        