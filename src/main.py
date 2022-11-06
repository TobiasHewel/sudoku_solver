"""This is the main file
"""
import sys
from pprint import pprint
from sudoku import solve


def run(sudoku_file_name: str):
    """Runs the program

    Parameters:
    -------
        - sudoku_file_name (str): The name of the sudoku file
    """
    with open("res/sudokus/" + sudoku_file_name, "r", encoding="UTF-8") as sudoku_file:
        sudoku = tuple([[letter for letter in row if letter != "\n"] for row in sudoku_file.readlines()])

    pprint(sudoku, width=50)

    solved_sudoku = solve(sudoku)


if __name__ == "__main__":
    run(
        sudoku_file_name=sys.argv[1] if len(sys.argv) > 1 else "example.txt"
    )
