"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        def intervals_overlap(interval_a, interval_b) -> bool:
            if interval_a.start < interval_b.end and interval_b.start < interval_a.end:
                return True
            return False

        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        left, right = 0,1
        while right < len(sorted_intervals):
            interval_1 = sorted_intervals[left]
            interval_2 = sorted_intervals[right]
            if intervals_overlap(interval_1, interval_2):
                return False
            left+=1
            right+=1
        return True


