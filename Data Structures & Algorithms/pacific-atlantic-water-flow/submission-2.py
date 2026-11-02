import sys
sys.setrecursionlimit(10000)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        atlantic = set()
        pacific = set()

        def dfs(r, c, visited, prev):
            if not (0 <= r < rows and 0 <= c < cols): return
            if (r, c) in visited or heights[r][c] < prev: return
            visited.add((r, c))
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                dfs(r+dr, c+dc, visited, heights[r][c])

        border_coordinates = {
            (r, c) for r in range(rows) for c in range(cols)
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1
        }

        for r,c in border_coordinates:
            if r == 0 or c == 0:
                dfs(r,c,pacific, heights[r][c])
            if r == rows -1 or c == cols - 1:
                dfs(r,c, atlantic, heights[r][c])

        return [[r, c] for r, c in atlantic & pacific]

    

    