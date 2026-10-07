from engine.board import board
from config import white_to_move, empty_cell


def is_move_legal(move_from: tuple[int], move_to: tuple[int]) -> bool:
    move_from_y = move_from[0]
    move_from_x = move_from[1]
    move_to_y = move_to[0]
    move_to_x = move_to[1]

    cell_moving_from: str = board[move_from_y][move_from_x]
    cell_moving_to: str = board[move_to_y][move_to_x]

    print(f"{cell_moving_from=}")
    print(f"{cell_moving_to=}")

    should = 'w' if white_to_move else 'b'
    if cell_moving_from[0] != should:
        return False

    if cell_moving_to[0] != should:
        return False

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
            if cell_moving_from[1] == "R":
                return False
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
    

