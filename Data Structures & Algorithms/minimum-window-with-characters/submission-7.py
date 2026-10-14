from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(s) < len(t):
            return ""
        left = 0
        min_len = float('inf')
        t_chars = Counter(t)
        curr_counts = Counter()
        candidate = ""
        need = len(t_chars)
        have = 0
        for right in range(len(s)):
            curr_counts[s[right]]+=1
            if s[right] in t_chars and curr_counts[s[right]] == t_chars[s[right]]:
                have += 1
            while have == need:
                if (right-left)+1 < min_len:
                    candidate = s[left:right+1]
                    min_len = (right-left)+1 
                curr_counts[s[left]]-=1
                if s[left] in t_chars and curr_counts[s[left]] < t_chars[s[left]]:
                    have -= 1
                left+=1
        return candidate

        
        