class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows, n_cols = len(matrix), len(matrix[0])
        low = 0
        high = n_rows*n_cols -1
        while low <= high:
            mid_idx = (low + high) // 2
            mid_r = mid_idx // n_cols
            mid_c = mid_idx % n_cols
            mid_cell = matrix[mid_r][mid_c]
            if mid_cell == target:
                return True
            elif target > mid_cell:
                low = mid_idx+1
            else:
                high = mid_idx-1
        return False



        