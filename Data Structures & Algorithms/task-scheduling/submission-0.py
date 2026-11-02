
from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        heap = [-c for c in counts.values()]

        heapq.heapify(heap)
        cool_down = deque()

        ticks = 0
        while heap or cool_down:
            ticks+=1
            if heap:
                task_count = heapq.heappop(heap)
                task_count+=1
                if task_count < 0:
                    cool_down.append((task_count, ticks + n))
            if cool_down:
                count, time = cool_down[0]
                if time == ticks:
                    heapq.heappush(heap, count)
                    cool_down.popleft()
            
        return ticks
            


        
        