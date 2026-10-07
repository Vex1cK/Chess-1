board = [
    ['bR', "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP"] * 8,
    ["  "] * 8,
    ["  "] * 8,
    ["  "] * 8,
    ["  "] * 8,
    ["wP"] * 8,
    ['wR', "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]

def do_move(move_from: tuple[int], move_to: tuple[int]):
    global board

    board[move_to[0]][move_to[1]] = board[move_from[0]][move_from[1]]
    board[move_from[0]][move_from[1]] = "  "

E = 4
E2 = -1 -4