import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = lambda x_1, y_1: math.sqrt(x_1**2 + y_1**2) 
        distances = [(distance(x_1, y_1), index) for index, (x_1, y_1) in enumerate(points)]
        heapq.heapify(distances)
        smallest = heapq.nsmallest(k, distances)
        indices = [small[1] for small in smallest]
        return [points[i] for i in indices]
        



        