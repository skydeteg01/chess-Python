
class Pawn:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def print_pawn(self):
        column, row = self.position
        print(f"Я пешка {self.color} цвета и стою на {column, row}")

    def can_move(self, target_position, board):
        column_from, row_from = self.position
        column_to, row_to = target_position

        direction = 0
        if self.color == "white":
            direction -=1
        else:
            direction +=1

        if column_from == column_to and row_from + direction == row_to and board[row_to][column_to] == " ":
            return True
        return False
