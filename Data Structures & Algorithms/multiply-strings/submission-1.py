class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                product = digit1*digit2 
                pos1 = i + j
                pos2 = i + j + 1
                total_sum = product + result[pos2]
                result[pos2] = total_sum % 10
                result[pos1] += total_sum // 10

        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(map(str, result[start:]))


     
        