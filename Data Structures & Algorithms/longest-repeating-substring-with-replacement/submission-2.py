from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
      
                
        left, max_len, max_freq = 0,0,0
        counts = Counter()
        
        for right in range(len(s)):
            counts[s[right]]+=1
            max_freq = max(max_freq, counts[s[right]])
            while (right-left+1) - max_freq > k:
                counts[s[left]]-=1
                left+=1
            max_len = max(max_len, right-left+1)
        return max_len
            



        