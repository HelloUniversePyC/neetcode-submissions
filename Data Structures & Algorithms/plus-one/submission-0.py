class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        joined_num = "".join(map(str,digits))
        increment = int(joined_num)+1
        return [int(digit) for digit in str(increment)]
        