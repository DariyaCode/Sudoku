import random

def solve_sudoku(puzzle):
    empty_cell = find_empty_cell(puzzle)
    if not empty_cell:
        return puzzle

    row, col = empty_cell

    numbers = list(range(1, 10))  # Числа от 1 до 9

    random.shuffle(numbers)  # Перемешиваем числа в случайном порядке

    for num in numbers:
        if is_valid_move(puzzle, row, col, num):
            puzzle[row][col] = num

            if solve_sudoku(puzzle):
                return puzzle

            puzzle[row][col] = 0

    return None


def is_valid_move(puzzle, row, col, num):
    # Проверка в строке
    for i in range(9):
        if puzzle[row][i] == num:
            return False

    # Проверка в столбце
    for i in range(9):
        if puzzle[i][col] == num:
            return False

    # Проверка внутри квадрата 3x3
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if puzzle[start_row + i][start_col + j] == num:
                return False

    return True

def find_empty_cell(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku(difficulty):
    puzzle = [[0] * 9 for _ in range(9)]
    solve_sudoku(puzzle)
    remove_cells(puzzle, difficulty)
    return puzzle

def remove_cells(puzzle, difficulty):
    num_empty_cells = get_num_empty_cells(difficulty)
    empty_cells = random.sample(range(81), num_empty_cells)  # Удаление нужного количества ячеек
    for cell in empty_cells:
        row = cell // 9
        col = cell % 9
        puzzle[row][col] = 0

def get_num_empty_cells(difficulty):
    if difficulty == 'Easy':
        return random.randint(35, 45)
    elif difficulty == 'Medium':
        return random.randint(46, 55)
    elif difficulty == 'Hard':
        return random.randint(56, 64)
    else:
        raise ValueError("Invalid difficulty level")
