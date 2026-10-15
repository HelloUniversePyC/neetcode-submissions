class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]* len(temperatures)
        indices = []
        for i,temp in enumerate(temperatures):
            while indices and temperatures[indices[-1]] < temp:
                removed_idx = indices.pop()
                output[removed_idx] = i- removed_idx # days to warmer
            indices.append(i)
        return output