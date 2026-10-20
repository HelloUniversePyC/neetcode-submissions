import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda x_1, y_1: -(x_1**2 + y_1**2)
        heap = []
        for x, y in points:
            heapq.heappush(heap, (distance(x,y), [x,y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [point for _, point in heap]

        



        