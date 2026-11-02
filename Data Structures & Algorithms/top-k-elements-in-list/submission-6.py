import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = Counter(nums)
        heap = []
        for elem,freq in frequency.items():
            heapq.heappush(heap, (freq, elem))
            while len(heap) > k:
                heapq.heappop(heap)
        return [val[1] for val in heap]


        