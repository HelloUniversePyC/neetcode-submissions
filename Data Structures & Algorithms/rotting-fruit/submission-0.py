from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        n_rows = len(grid)
        n_cols = len(grid[0])


        for r in range(n_rows):
            for c in range(n_cols):
                curr_fruit = grid[r][c]
                if curr_fruit == 2:
                    q.append((r,c))
                if curr_fruit == 1:
                    fresh+=1
        
        if (fresh == 0 and not q) or len(q) == (n_rows*n_cols):
            return 0
        if fresh == (n_rows*n_cols):
            return -1

        minutes = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                for neighbor in [(r+1, c), (r-1, c), (r,c+1), (r,c-1)]:
                    r_2, c_2 = neighbor
                    if r_2 >= n_rows or r_2 < 0 or c_2 >= n_cols or c_2 < 0:
                        continue
                    if grid[r_2][c_2] == 1:
                        grid[r_2][c_2] = 2
                        fresh-=1
                        q.append(neighbor)
             
            minutes+=1
        return minutes if fresh == 0 else -1
            


        