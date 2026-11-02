class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        for i in range(n_rows):
            for j in range(i+1,n_cols):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()

        