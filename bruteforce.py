import termcolor
import os
import sys
import time

test_case = [
    [1, 0, 0, 2, 0, 3, 5, 7, 6],
    [0, 0, 6, 0, 5, 0, 0, 0, 4],
    [5, 3, 7, 0, 0, 0, 0, 0, 1],
    [4, 0, 9, 0, 0, 0, 1, 6, 2],
    [6, 1, 0, 0, 4, 0, 0, 0, 7],
    [0, 8, 0, 6, 2, 1, 9, 0, 0],
    [0, 6, 0, 0, 0, 0, 4, 5, 9],
    [0, 7, 5, 0, 1, 0, 0, 2, 8],
    [2, 0, 4, 0, 0, 5, 7, 0, 3]
]

class Get:
    def __init__(self, sudoku):
        self.sudoku = sudoku

    def get_available_from_row(self, row):
        nums = set(range(1, 10))  # Use set for efficient removal
        for num in self.sudoku[row]:
            nums.discard(num)  # discard removes the element if it exists, does nothing otherwise
        return nums
    
    def get_available_from_col(self, col):
        nums = set(range(1, 10))
        for row in self.sudoku:
            nums.discard(row[col])
        return nums
    
    def get_available_from_cube(self, col, row):
        nums = set(range(1, 10))
        start_row = (row // 3) * 3
        start_col = (col // 3) * 3
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                nums.discard(self.sudoku[r][c])
        return nums

    def get_possible_nums(self, row, col):
        # Use set intersection (&) to find common elements in all three sets
        possible_nums = self.get_available_from_row(row) & self.get_available_from_col(col) & self.get_available_from_cube(col, row)
        return list(possible_nums)

def print_sudoku(sudoku):
    os.system('cls' if os.name == 'nt' else 'clear')
    for r in sudoku:
        print(' '.join([str(num) for num in r]))

def print_sudoku_highlighted(highlight_row, highlight_col, sudoku, note=''):
    os.system('cls' if os.name == 'nt' else 'clear')

    for r_idx, row in enumerate(sudoku):
        for c_idx, cell in enumerate(row):
            if cell == 0:
                cell = termcolor.colored(cell, on_color="on_light_red")
            if r_idx == highlight_row and c_idx == highlight_col:
                cell = termcolor.colored(cell, on_color="on_cyan")
            sys.stdout.write(f' {cell}')
            sys.stdout.flush()
        sys.stdout.write('\n')
        sys.stdout.flush()
    sys.stdout.write(termcolor.colored(note, color="cyan") + '\n')
    sys.stdout.flush()


def find_first_zero(sudoku):
    for r in range(len(sudoku)):
        for c in range(len(sudoku[r])):
            if sudoku[r][c] == 0:
                return r, c
    return -1, -1

def solve_sudoku(sudoku):
    r, c = find_first_zero(sudoku)
    if r == -1 and c == -1:
        return True  # Puzzle is solved

    fetch = Get(sudoku)
    possible_nums = fetch.get_possible_nums(r, c)

    for num in possible_nums:
        sudoku[r][c] = num
        # time.sleep(0.2)
        print_sudoku_highlighted(r, c, sudoku)
        if solve_sudoku(sudoku):
            return True
        sudoku[r][c] = 0  # Backtrack
        # time.sleep(0.2)
        print_sudoku_highlighted(r, c, sudoku, note="Backtracking...")

    return False

if solve_sudoku(test_case):
    print("Solved Sudoku:")
    print_sudoku(test_case)
else:
    print("No solution exists")
