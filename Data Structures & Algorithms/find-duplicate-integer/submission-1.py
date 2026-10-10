class Solution:
    from collections import Counter
    def findDuplicate(self, nums: List[int]) -> int:
        list_counts = Counter(nums)
        duplicate = -1
        for i,count in list_counts.items():
            if count > 1:
                duplicate = i
        return duplicate
        
       

        