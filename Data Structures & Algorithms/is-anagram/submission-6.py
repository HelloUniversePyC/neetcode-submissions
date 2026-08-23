class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_dict = {char: s.count(char) for char in s}
        for char in t:
            if char in counts_dict:
                counts_dict[char]-=1
        return all(value == 0 for value in counts_dict.values())
        
        