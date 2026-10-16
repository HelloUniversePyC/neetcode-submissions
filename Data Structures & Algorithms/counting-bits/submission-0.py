class Solution:
    def countBits(self, n: int) -> List[int]:
        def hammingWeight(n: int) -> int:
            one_counter = 0
            for i in range(32):
                bit = (n >> i) & 1
                if bit == 1:
                    one_counter+=1
            return one_counter
        output = []
        for i in range(n+1):
            output.append(hammingWeight(i))
        return output

        