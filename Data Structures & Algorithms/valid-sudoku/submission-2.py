class Solution:

    # Only check for duplicates in row, column, and grid
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Step 1: Check Row
        for sublist in board:
            row_check = {}

            for item in sublist:
                if item == ".": 
                    continue
                if item in row_check:
                    print("duplicate found in ROWS") 
                    return False
                else:
                    row_check[item] = 1
                
        print("========= Row Check Clear =========")
        

        
        # Step 2: Check Column
        for col in range(len(board)):
            col_check = {}
            for row in range(len(board)):
                item = board[row][col]
                if item == ".":
                    continue
                if item in col_check:
                    print("duplicate found in COLUMNS")
                    return False
                else:
                    col_check[item] = 1    

        print("========= Col Check Clear =========")

        # Step 3: Check squares
        square_check = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                # If the current item is a dot, skip it
                if board[row][col] == ".":
                    continue
                # Get current square
                curr_square = (row // 3) * 3 + (col // 3)
                value = board[row][col]

                # Initialize this square if it doesn't exist
                if curr_square not in square_check:
                    square_check[curr_square] = {}

                # Check if value is in our square
                if value in square_check[curr_square]:
                    print("duplicate found in SQUARES")
                    return False
                else:
                    square_check[curr_square][value] = 1




        return True