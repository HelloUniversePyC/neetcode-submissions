from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        curr_window = deque()
        max_array = []
        for i,num in enumerate(nums):
            if curr_window and curr_window[0] < i-k+1:
                curr_window.popleft()
            while curr_window and nums[curr_window[-1]] < num:
                curr_window.pop()
            curr_window.append(i)

            if i >= k-1:
                max_array.append(nums[curr_window[0]])
        return max_array
        