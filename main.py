#chess

board = [
    ["br","bn","bb","bq","bk","bb","bn","br"],
    ["bp","bp","bp","bp","bp","bp","bp","bp"],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "," "],
    ["wp","wp","wp","wp","wp","wp","wp","wp"],
    ["wr","wn","wb","wq","wk","wb","wn","wr"]
]

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]

def print_board(board):
    for index, row in enumerate(board):
        print(8 - index, end=" ")
        for cell in row:
            print( cell, end=" ")
        print('')
    for letter in letters:
        print(' ', letter, end="")
print_board(board)

print(" ")
move = input("Enter your move: ")
move_s = move.split()
from_square = move_s[0]
to_square = move_s[1]
print(from_square[0])
print(from_square[1])
column = letters.index(from_square[0])
row = 8 - int(from_square[1])

print(board[row][column])