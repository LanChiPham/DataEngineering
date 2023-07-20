### 7. Backtracking algorithm:
# The N-Queens Problem: The N-Queens problem is a classic problem that can be solved using backtracking. The goal is to place N queens on an NxN chessboard in such a way that no queen can attack any other queen.


def solveNQueens(n):
    def could_place(row, col):
        # check if a queen can be placed on board[row][col]
        # check if this row is not under attack from any previous queen in that column
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

def backtrack(row=0, count=0):
        for col in range(n):
            if could_place(row, col):
                board[row] = col
                if row + 1 == n:
                    count += 1
                else:
                    count = backtrack(row + 1, count)
        return count
#     board = [-1 for x in range(n)]
#     return backtrack()
# print(solveNQueens(4))

#This algorithm starts placing queens in the first row, and for every placed queen it checks if it is under attack from any previous queen. 
# If not, it proceeds to the next row and repeats the process. 
# If a queen is placed in a position where it is under attack, the algorithm backtracks and tries a different position. 
# This continues until all queens are placed on the board without any attacking each other.
