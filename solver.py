import random

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
    for r in sudoku:
        print(' '.join([str(num) if num != 0 else '.' for num in r]))
    print()

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
        if solve_sudoku(sudoku):
            return True
        sudoku[r][c] = 0  # Backtrack

    return False

# Example test case
test_case = [
    [0, 6, 4, 3, 0, 9, 2, 1, 8],
    [8, 2, 0, 0, 0, 0, 7, 0, 9],
    [0, 7, 3, 0, 1, 0, 4, 0, 0],
    [6, 0, 0, 0, 0, 0, 5, 0, 1],
    [3, 5, 7, 8, 0, 0, 0, 9, 4],
    [1, 4, 0, 7, 0, 6, 3, 0, 2],
    [0, 0, 5, 0, 8, 7, 0, 0, 0],
    [0, 3, 0, 6, 9, 0, 1, 0, 7],
    [0, 0, 6, 0, 0, 2, 0, 4, 0]
]

print("Initial Sudoku:")
print_sudoku(test_case)

if solve_sudoku(test_case):
    print("Solved Sudoku:")
    print_sudoku(test_case)
else:
    print("No solution exists")
