import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(rate: int) -> bool:
            total = 0
            for pile in piles:
                eating_time = math.ceil(pile / rate)
                total+=eating_time
            return total
        
        left,right = 1, max(piles)

        while(left < right):
            mid = (left + right) //2
            if can_eat(mid) <= h:
                right = mid
            else:
                left = mid+1
        return left
            

        