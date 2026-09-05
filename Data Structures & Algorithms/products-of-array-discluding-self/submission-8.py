class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Step 1. Make prefix array
        output = [1]*len(nums)
        prefix = 1
        for i,num in enumerate(nums):
            output[i] = prefix
            prefix*=num
        #Step 2. multiply by remaining suffix
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i]*= suffix
            suffix*=nums[i]
        return output

        
        
           
        