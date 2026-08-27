class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_stand_case = s.lower()
        left = 0
        right = len(s)-1
        while left < right:
            #Skip over not alpha on the left
            while left < right and not s_stand_case[left].isalnum():
                left+=1
            #Skip over not alpha on the right
            while left < right and not s_stand_case[right].isalnum():
                right-=1
            if (s_stand_case[left] != s_stand_case[right]):
                return False
            left+=1
            right-=1
        return True
        