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

def print_board(board): # Печатает доску
    for index, row in enumerate(board):
        print(8 - index, end=" ")
        for cell in row:
            print( cell, end=" ")
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

def can_move(figure, piece):
    if figure != " ":
        if piece == " " or piece[0] != figure[0]:
            return True
        else:
            return False
    else:
        return False

def make_move(board, column_from, row_from, column_to, row_to):
    figure = board[row_from][column_from] # Получаем фгуру которая будет ходить
    piece = board[row_to][column_to] # Место куда будет сделан ход
    if can_move(figure, piece): # Возвращает можно ли сделать ход
        board[row_to][column_to] = figure # Клетку куда мы должны сходить заменяем фигурой
        board[row_from][column_from] = " " # Клетку который мы ходили оставляем пустой

print(" ")
while True:

    from_square, to_square = get_move() # Воозвращает откуда делается ход и куда

    column_from, row_from = square_to_position(from_square) # Возвращает индексы координат
    column_to, row_to = square_to_position(to_square)

    make_move(board, column_from, row_from, column_to, row_to) # Делает само передвижение

    print_board(board)
