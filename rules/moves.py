from config import white_to_move, bukvi, chiferki, letter_to_index


def transform_user_data(got_from_user: list[str]):
    res = []
    for el in got_from_user:
        res.append((8 - int(el[1]), letter_to_index[el[0]]))
    return res

def get_move_from_user():
    print(f"Сейчас ходят: {"белые" if white_to_move else "черные"}\n")
    got_from_user = input("Ввод: ")
    print(f"{got_from_user=}")
    print(bool(got_from_user))
    print("\n")
    if got_from_user == "выход":
        return False, got_from_user
    if not got_from_user:
        return False, None

    got_from_user = got_from_user.split()

    if len(got_from_user) != 2 or \
            len(got_from_user[0]) != 2 or \
            len(got_from_user[1]) != 2 or \
            got_from_user[0][0] not in bukvi or \
            got_from_user[1][0] not in bukvi or \
            got_from_user[0][1] not in chiferki or \
            got_from_user[1][1] not in chiferki:
        return False, None

    return True, transform_user_data(got_from_user)

