"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])
        start_pntr = 0
        end_pntr = 0
        n_rooms = 0
        max_rooms = 0
        while end_pntr < len(end_times) and start_pntr < len(start_times):
            if start_times[start_pntr] < end_times[end_pntr]:
                n_rooms+=1
                start_pntr+=1
            else:
                n_rooms-=1
                end_pntr+=1
            max_rooms = max(n_rooms, max_rooms)
        return max_rooms

