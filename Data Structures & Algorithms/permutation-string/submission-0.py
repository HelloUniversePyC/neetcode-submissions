from collections import Counter,deque
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        curr_window = deque()
        remaining_chars = Counter(s1)
        window_count = Counter()
        k = len(s1)
        for r,char in enumerate(s2):
            curr_window.append(char)
            window_count[char]+=1
            if len(curr_window) > k:
                left_char = curr_window.popleft()
                window_count[left_char]-=1
                if window_count[left_char] == 0:
                    del window_count[left_char]
            if len(curr_window) == k:
                if window_count == remaining_chars:
                    return True 
        return False
            