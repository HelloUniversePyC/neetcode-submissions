class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        target_vals = {i for i in range(1,10)}
        target_vals.add(".")

        def valid_3_by_3(board_slice) -> bool:
            seen = set()
            for i in range(len(board_slice)):
                for j in range(len(board_slice[i])):
                    cell = board_slice[i][j]
                    if cell in seen and cell != ".":
                        return False
                    else:
                        seen.add(cell)
            return seen | target_vals != {}
        
        #Check rows
        for i,row in enumerate(board):
            row_seen = set()
            for elem in row:
                if elem in row_seen and elem != ".":
                    return False
                else:
                    row_seen.add(elem)

            if row_seen | target_vals == {}:

                return False
        
        #Check columns
        col_seen = set()
        for col_idx in range(len(board)):
            col_seen = set()
            for row_idx in range(len(board)):
                elem = board[row_idx][col_idx]
                if elem in col_seen and elem != ".":
                    return False
                else:
                    col_seen.add(elem)
            if col_seen | target_vals == {}:
                return False
        
        #Check boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                box = []
                for r in range(i, i + 3):
                    mini_board = [board[r][j:j + 3] for r in range(i, i + 3)]
                    if not valid_3_by_3(mini_board):
                        return False
        return True


            
                
        


            
        






        