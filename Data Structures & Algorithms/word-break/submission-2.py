class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = dict()
        def dfs(i):
            if i == len(s):
                return True
            if i in self.memo:
                return self.memo[i]
            for word in wordDict:
                if s.startswith(word, i) and dfs(i+len(word)):
                    self.memo[i] = True
                    return True
            self.memo[i] = False
            return False
        return dfs(0)
        