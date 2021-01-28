import numpy as np

ROW_COUNT = 6
COULMN_COUNT = 7

def create_board():
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, column, checker):
    board[row][column] = checker

def is_valid_location(board, column):
    return board[5][column] == 0

def get_next_open_row(board, column):
    for r in range(ROW_COUNT):
        if board[r][column] == 0:
            return r
def print_board(board):
    print(np.flip(board, 0))

board = create_board()
game_over = False
turn = 0
print_board(board)

while not game_over:
    if turn == 0: #Ask for play 1 input
        column = int(input("Player 1: Make Selection (0-6):"))
        print(column)
        if is_valid_location(board, column):
            row= get_next_open_row(board, column)
            drop_piece(board, row, column, 1)
    else: 
        column = int(input("Player 2: Make Selection (0-6):"))
        if is_valid_location(board, column):
            row= get_next_open_row(board, column)
            drop_piece(board, row, column, 2)
    print_board(board)       
    turn += 1
    turn = turn % 2 #Makes it so the players alternate