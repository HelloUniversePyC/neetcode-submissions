class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        inserted = []
        new_start, new_end = newInterval
        i = 0
        n_intervals = len(intervals)
        
        #1. Add all intervals that end before the new interval starts.
        while i < n_intervals:
            curr_start, curr_end = intervals[i]
            if curr_end < new_start:
                inserted.append(intervals[i])
            else:
                break
            i+=1
        
        #2. Merge all overlapping intervals into one single newInterval
        while i < n_intervals:
            curr_start, curr_end = intervals[i]
            if curr_start <= new_end:
                new_start = min(new_start, curr_start)
                new_end = max(new_end, curr_end)
            else:
                break
            i += 1

        inserted.append([new_start, new_end])
            

        #3. Add all intervals that start after the new interval ends
        while i < n_intervals:
            inserted.append(intervals[i])
            i+=1
        
        return inserted
            

            

            

