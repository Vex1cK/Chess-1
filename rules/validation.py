from engine.board import board
from config import get_white_to_move, empty_cell


def is_nobody_on_the_path(move_from: tuple[int], move_to: tuple[int]):
    move_from_y = move_from[0]
    move_from_x = move_from[1]
    move_to_y = move_to[0]
    move_to_x = move_to[1]

    cell_moving_from: str = board[move_from_y][move_from_x]
    
    if cell_moving_from[1] not in ["K", "N"]:
        # print("cheking 1...")
        if move_from_x == move_to_x:
            # print("Tik")
            step = 1
            if move_from_y > move_to_y:
                step = -1
            for i in range(move_from_y+step, move_to_y, step):
                if board[i][move_from_x] != empty_cell:
                    return False
        elif move_from_y == move_to_y:
            # print("Tok")
            step = 1
            if move_from_x > move_to_x:
                step = -1
            for i in range(move_from_x+step, move_to_x, step):
                if board[move_from_y][i] != empty_cell:
                    return False
        else:
            if cell_moving_from[1] != "P":
                # (6, 4) -> (3, 1): +1 -1
                # (3, 1) -> (6, 4): +1 +1

                # (6, 4) -> (3, 7): -1 +1
                # (3, 7) -> (6, 4): -1 -1

                if abs(move_from_y - move_to_y) != abs(move_from_x - move_to_x):
                    return False

                step_0 = 1
                step_1 = 1
                if (move_to_y < move_from_y):
                    step_0 = -1
                if (move_to_x < move_from_x):
                    step_1 = -1

                for i in range(1, abs(move_from_y - move_to_y)):
                    new_x = move_from_y + (step_0 * i)
                    new_y = move_from_x + (step_1 * i)
                    if board[new_x][new_y] != empty_cell:
                        return False
    return True

def is_piece_moving_correctly(move_from: tuple[int], move_to: tuple[int]):
    taking_on_the_aisle = False

    move_from_y = move_from[0]
    move_from_x = move_from[1]
    move_to_y = move_to[0]
    move_to_x = move_to[1]

    false_return = (False, False)

    cell_moving_from: str = board[move_from_y][move_from_x]
    should = 'w' if get_white_to_move() else 'b'
    
    if cell_moving_from[1] == "R":
        if not (move_from_x == move_to_x or move_from_y == move_to_y):
            return false_return
    elif cell_moving_from[1] == "N":
        dx = abs(move_to_x - move_from_x)
        dy = abs(move_to_y - move_from_y)
        if dx * dy != 2:
            return false_return
    elif cell_moving_from[1] == "K":
        dx = abs(move_to_x - move_from_x)
        dy = abs(move_to_y - move_from_y)
        if max(dx, dy) != 1:
            return false_return
    elif cell_moving_from[1] == "B":
        dx = abs(move_to_x - move_from_x)
        dy = abs(move_to_y - move_from_y)

        if dx != dy:
            return false_return
    elif cell_moving_from[1] == "P":
        direction = -1 if should == 'w' else 1
        start_row = 6 if should == 'w' else 1
        dy = move_to_y - move_from_y
        dx = abs(move_to_x - move_from_x)

        move_y_is_ok = dy == direction or (dy == 2 * direction and move_from_y == start_row)
        if not move_y_is_ok:
            return false_return
        move_y = 1 if dy == direction else 2

        if move_y == 2 and dx != 0:
            return false_return
        elif move_y == 1 and dx not in [0, 1]:
            return false_return

        if dx == 1:
            taking_on_the_aisle = True
    elif cell_moving_from[1] == "Q":
        dx = abs(move_to_x - move_from_x)
        dy = abs(move_to_y - move_from_y)

        if not (move_from_x == move_to_x or move_from_y == move_to_y or dx == dy):
            return false_return

    return True, taking_on_the_aisle

def is_move_legal(move_from: tuple[int], move_to: tuple[int]) -> bool:
    """
    Проверяет что ход валидный

    move_from: tuple[int] - кортеж координат исходной клетки для обращения в board
    move_to: tuple[int] - кортеж координат итоговой клетки для обращения в board
    move_from и move_to не должны выходить на пределы доски!

    return bool
    """
    move_from_y = move_from[0]
    move_from_x = move_from[1]
    move_to_y = move_to[0]
    move_to_x = move_to[1]

    cell_moving_from: str = board[move_from_y][move_from_x]
    cell_moving_to: str = board[move_to_y][move_to_x]

    # print(f"{cell_moving_from=}")
    # print(f"{cell_moving_to=}")

    should = 'w' if get_white_to_move() else 'b'
    if cell_moving_from[0] != should:
        return False

    if cell_moving_to[0] == should:
        return False

    if move_from == move_to:
        return False

    ok, taking_on_the_aisle = is_piece_moving_correctly(move_from, move_to)
    if not ok:
        return False

    ok = is_nobody_on_the_path(move_from, move_to)
    if not ok:
        return False

    return True
    

