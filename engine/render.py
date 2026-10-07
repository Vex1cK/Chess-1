from config import bukvi, chiferki, instruction
from engine.board import board

def print_board():
    print(f"", *bukvi, sep="    ", end='   \n')
    print(" ", "-"*41)
    for row, i, instr in zip(board, chiferki[::-1], instruction):
        print(f"{i}", *row, sep=" | ", end=f' | {i}')
        print("\t\t\t", instr)
        print(" ", "-"*41)
    print(f"", *bukvi, sep="    ", end='   \n')
    print("\n")