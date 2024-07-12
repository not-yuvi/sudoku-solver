import random

class SudokuGenerator:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    
    def is_valid(self, num, row, col):
        # Check if num is not in the current row
        if num in self.grid[row]:
            return False
        
        # Check if num is not in the current column
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        
        # Check if num is not in the current 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        
        return True
    
    def fill_grid(self):
        # Backtracking algorithm to fill the grid
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Define the numbers list
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(num, row, col):
                            self.grid[row][col] = num
                            if self.fill_grid():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True
    
    def remove_numbers(self, difficulty):
        # Difficulty: 0 (easy) to 1 (hard)
        cells_to_remove = int(81 * difficulty)
        while cells_to_remove > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            self.grid[row][col] = 0
            cells_to_remove -= 1
    
    def generate_puzzle(self, difficulty=0.5):
        self.fill_grid()
        self.remove_numbers(difficulty)
        return self.grid

# Usage
generator = SudokuGenerator()
sudoku_puzzle = generator.generate_puzzle(difficulty=0.5)

# Print the Sudoku puzzle
for row in sudoku_puzzle:
    if row != sudoku_puzzle[-1]:
        print(f'{row},')
    else:
        print(row)

