"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        for interval in sorted_intervals:
            start = interval.start
            end = interval.end
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            heapq.heappush(heap,end)
        return len(heap)



        