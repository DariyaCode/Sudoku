import time
import random

# Global variables
EMPTY = 0
GRID_SIZE = 9
BOX_SIZE = 3

# Function to print the Sudoku grid
def print_grid(grid):
    for i in range(GRID_SIZE):
        if i % BOX_SIZE == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(GRID_SIZE):
            if j % BOX_SIZE == 0 and j != 0:
                print("| ", end="")
            print(grid[i][j], end=" ")
        print()

# Function to check if the given number is valid in the given position
def is_valid(grid, row, col, num):
    # Check if the number already exists in the row
    for i in range(GRID_SIZE):
        if grid[row][i] == num:
            return False

    # Check if the number already exists in the column
    for i in range(GRID_SIZE):
        if grid[i][col] == num:
            return False

    # Check if the number already exists in the box
    box_row = (row // BOX_SIZE) * BOX_SIZE
    box_col = (col // BOX_SIZE) * BOX_SIZE
    for i in range(BOX_SIZE):
        for j in range(BOX_SIZE):
            if grid[box_row + i][box_col + j] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == EMPTY:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True

                        grid[row][col] = EMPTY

                return False

    return True

# Function to generate a Sudoku puzzle of a given difficulty level
def generate_puzzle(difficulty):
    grid = [[EMPTY] * GRID_SIZE for _ in range(GRID_SIZE)]
    solve_sudoku(grid)

    # Remove random cells to create the puzzle
    num_cells = GRID_SIZE * GRID_SIZE
    num_empty_cells = int(num_cells * difficulty / 100)
    empty_cells = random.sample(range(num_cells), num_empty_cells)

    for cell in empty_cells:
        row = cell // GRID_SIZE
        col = cell % GRID_SIZE
        grid[row][col] = EMPTY

    return grid

# Function to play the Sudoku game
def play_sudoku(difficulty):
    grid = generate_puzzle(difficulty)
    start_time = time.time()

    print_grid(grid)

    while True:
        row = int(input("Enter the row (1-9): ")) - 1
        col = int(input("Enter the column (1-9): ")) - 1
        num = int(input("Enter the number (1-9): "))

        # Input validation
        if not (1 <= row <= GRID_SIZE and 1 <= col <= GRID_SIZE and 1 <= num <= GRID_SIZE):
            print("Invalid input! Please enter values within the range 1-9.")
            continue

        if is_valid(grid, row, col, num):
            grid[row][col] = num
        else:
            print("Invalid move! Please try again.")
            continue

        print_grid(grid)

        if solve_sudoku(grid):
            print("Congratulations! You solved the puzzle.")
            end_time = time.time()
            elapsed_time = end_time - start_time
            print("Elapsed Time: {:.2f} seconds".format(elapsed_time))
            break

# Main program
def main():
    print("Welcome to Sudoku!")

    while True:
        print("\nSelect the difficulty level:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))

        if choice == 1:
            play_sudoku(40)  # Easy difficulty: 40% filled cells
        elif choice == 2:
            play_sudoku(30)  # Medium difficulty: 30% filled cells
        elif choice == 3:
            play_sudoku(20)  # Hard difficulty: 20% filled cells
        elif choice == 4:
            print("Thank you for playing Sudoku!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
