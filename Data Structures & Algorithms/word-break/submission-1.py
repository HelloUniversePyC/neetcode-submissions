class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.memo = dict()
        def dfs(i):
            if i == len(s):
                return True
            if i in self.memo:
                return self.memo[i]
            for word in wordDict:
                if s.startswith(word, i):
                    self.memo[(i+len(word))] = dfs(i+len(word))
                    if self.memo[(i+len(word))] == True:
                        return True
            return False
        return dfs(0)
        