from engine.render import print_board
from rules.moves import get_move_from_user
from rules.validation import is_move_legal


def main():
    print("Привет! ты запустил шахматы, вот тебе доска:\n\n")
    while True:
        while True:
            print_board()
            ok, got_from_user = get_move_from_user()
            if ok:
                # print("OK!")
                break
            if not ok:
                if got_from_user is None:
                    continue
                elif got_from_user == "выход":
                    print("Выход..")
                    return 0
        is_move_ok = is_move_legal(*got_from_user)
        if not is_move_ok:
            print("Ты ввёл какую-дичь, так ходить нельзя!")
            continue
        if is_move_ok:
            print("move is OK!")



if __name__ == "__main__":
    main()