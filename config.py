instruction = [
    "",
    "",
    "Чтобы сделать ход напиши {буква}{цифра} {буква}{цифра}",
    "Например: E2 E4 (регистр не важен, буква+цифра писать слитно!)",
    "",
    'Напишите "выход" чтобы закончить игру',
    "",
    "",
]

white_to_move = True
bukvi = ["A", "B", "C", "D", "E", "F", "G", "H"]
chiferki = list(map(str, range(1, 9)))
empty_cell = "  "
quiting_on = ["выход", "quit", '-']

letter_to_index = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}

def change_moving_color():
    global white_to_move
    white_to_move = not white_to_move
    print(f"Changed: white_to_move now equal {white_to_move}")

def get_white_to_move():
    global white_to_move
    return white_to_move