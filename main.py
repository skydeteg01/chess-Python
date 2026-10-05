#chess
from Pieces import Pawn

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

def print_board(board): # Печатает доску
    for index, row in enumerate(board):
        print(8 - index, end=" ")
        for cell in row:
            if cell == " ":
                cell = ". "
            print(cell, end=" ")
        print('')
    for letter in letters:
        print(' ', letter, end="")
print_board(board)


def get_move(): # Сделать ход
    move = input("Enter your move: ")
    move_s = move.split()
    from_square = move_s[0]
    to_square = move_s[1]
    return from_square, to_square


def square_to_position(square): # Преобразует координаты в индексы
    column = letters.index(square[0]) # Ищет порядковый номер буквенной координвты
    row = 8 - int(square[1]) # Ищет номер строки
    return column, row


def can_move(figure, piece, column_from, row_from, column_to, row_to, board):
    if figure[1] == "p":
        if figure[0] == "w":
            return pawn_can_move(figure, piece, column_from, row_from, column_to, row_to, board)
        if figure[0] == "b":
            return pawn_can_move(figure, piece, column_from, row_from, column_to, row_to, board)
    return False


def pawn_can_move(figure, piece, column_from, row_from, column_to, row_to, board):
    if figure[0] == "w":
        if column_from == column_to and row_to == row_from - 1 and piece == " ":
            return True
        if row_from == 6 and row_to == row_from - 2 and board[row_from - 1][column_to] == " " and column_from == column_to and piece == " ":
            return True
        if row_to == row_from - 1 and abs(column_to - column_from) == 1 and piece != " " and piece[0] == "b":
            return True
    if figure[0] == "b":
        if column_from == column_to and row_to == row_from + 1 and piece == " ":
            return True
        if row_from == 1 and row_to == row_from + 2 and board[row_from + 1][column_to] == " " and column_from == column_to and piece == " ":
            return True
        if row_to == row_from + 1 and abs(column_to - column_from) == 1 and piece != " " and piece[0] == "w":
            return True
    return False


def make_move(board, column_from, row_from, column_to, row_to):
    figure = board[row_from][column_from] # Получаем фгуру которая будет ходить
    piece = board[row_to][column_to] # Место куда будет сделан ход
    if can_move(figure, piece, column_from, row_from, column_to, row_to, board): # Возвращает можно ли сделать ход
        board[row_to][column_to] = figure # Клетку куда мы должны сходить заменяем фигурой
        board[row_from][column_from] = " " # Клетку который мы ходили оставляем пустой

wp1 = Pawn("White", (4,6))
print(wp1.can_move((4,5), board))

while True:
    print(" ")
    from_square, to_square = get_move() # Воозвращает откуда делается ход и куда

    column_from, row_from = square_to_position(from_square) # Возвращает индексы координат
    column_to, row_to = square_to_position(to_square)

    make_move(board, column_from, row_from, column_to, row_to) # Делает само передвижение

    print_board(board)