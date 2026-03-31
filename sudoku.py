def print_board(board):
    for row in board:
        print(row)

def is_safe(board, r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    start_r, start_c = r - r % 3, c - c % 3
    for i in range(3):
        for j in range(3):
            if board[start_r+i][start_c+j] == num:
                return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_safe(board, r, c, num):
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

solve(board)
print("Solved Sudoku:")
print_board(board)