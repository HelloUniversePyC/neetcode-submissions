class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recursive_exponent(base, exp):
            if exp == 0:
                return 1.0
            
            half = recursive_exponent(base, exp //2)
            if exp % 2 == 0:
                return half*half
            else:
                return half*half*base
        
        if n < 0:
            return 1/recursive_exponent(x, abs(n))
        return recursive_exponent(x, n)
        
    
        