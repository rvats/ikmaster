def printSolution(board): 
    for i in range(len(board)): 
        for j in range(len(board)): 
            print(board[i][j], end=', ')
        print()

def isSafe(board, row, col): 
    # Check this row on left side 
    for i in range(col): 
        if board[row][i] == 1: 
            return False
    # Check upper diagonal on left side 
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    # Check lower diagonal on left side 
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False
    return True
  
def solveNQHelper(board, col): 
    # base case: If all queens are placed 
    # then return true 
    if col >= len(board): 
        return True
  
    # Consider this column and try placing 
    # this queen in all rows one by one 
    for i in range(len(board)): 
        if isSafe(board, i, col): 
            board[i][col] = 1
            if solveNQHelper(board, col + 1) == True: 
                return True
            board[i][col] = 0
    return False

def solveNQ(number): 
    board = [[0 for x in range(number)] for y in range(number)]   
    if solveNQHelper(board, 0):
        printSolution(board) 
        return True
    else:
        print("Solution does not exist")
        return False

# driver program to test above function 
for number in range(2,9):
    print(solveNQ(number))
    print("===============================================================")