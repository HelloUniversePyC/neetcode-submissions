class Solution:
    def isHappy(self, n: int) -> bool:
        max_iter = 100
        curr_iter = 0
        while curr_iter < max_iter:
            n = str(n)
            n = sum([int(digit)**2 for digit in n])
            if n == 1:
                return True
            curr_iter+=1
        return False