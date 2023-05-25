import tkinter as tk
from tkinter import messagebox
from sudoku_solver import solve_sudoku, generate_sudoku

class SudokuGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.timer_running = False
        self.timer_count = 0
        self.best_time = {'Easy': float('inf'), 'Medium': float('inf'), 'Hard': float('inf')}
        self.current_difficulty = 'Easy'

        # Создание сетки Sudoku
        self.cells = []
        for i in range(9):
            row = []
            for j in range(9):
                cell = tk.Entry(root, width=3, font=('Arial', 16, 'bold'), justify='center')
                cell.grid(row=i, column=j)
                row.append(cell)
            self.cells.append(row)

        # Кнопки
        solve_button = tk.Button(root, text='Показать решение', command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=9)

        difficulty_label = tk.Label(root, text='Уровень сложности:')
        difficulty_label.grid(row=10, column=0, columnspan=3)
        difficulty_var = tk.StringVar(root)
        difficulty_var.set('Easy')
        difficulty_menu = tk.OptionMenu(root, difficulty_var, 'Easy', 'Medium', 'Hard', command=self.change_difficulty)
        difficulty_menu.grid(row=10, column=3, columnspan=3)

        timer_label = tk.Label(root, text='Время:')
        timer_label.grid(row=11, column=0, columnspan=3)
        self.timer_var = tk.StringVar(root)
        self.timer_var.set('00:00')
        timer_value = tk.Label(root, textvariable=self.timer_var)
        timer_value.grid(row=11, column=3, columnspan=3)

        best_time_button = tk.Button(root, text='Лучшее время', command=self.show_best_time)
        best_time_button.grid(row=12, column=0, columnspan=9)

        # Запуск таймера
        self.start_timer()

        # Генерация новой игры
        self.new_game()

def new_game(self):
    # Сброс значений ячеек
    for i in range(9):
        for j in range(9):
            self.cells[i][j].delete(0, tk.END)
            self.cells[i][j].config(state='normal')

    # Сброс таймера
    self.timer_count = 0

    # Генерация новой судоку
    sudoku = generate_sudoku()
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] != 0:
                self.cells[i][j].insert(0, str(sudoku[i][j]))
                self.cells[i][j].config(state='disabled')

    def solve(self):
        # Получение значений ячеек
        puzzle = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                value = self.cells[i][j].get()
                if value.isdigit():
                    puzzle[i][j] = int(value)
                else:
                    puzzle[i][j] = 0

        # Решение судоку
        solved_puzzle = solve_sudoku(puzzle)

        # Отображение решения
        if solved_puzzle:
            for i in range(9):
                for j in range(9):
                    self.cells[i][j].delete(0, tk.END)
                    self.cells[i][j].insert(0, str(solved_puzzle[i][j]))
        else:
            messagebox.showinfo("Ошибка", "Невозможно решить судоку!")

    def start_timer(self):
        self.timer_count += 1
        minutes = self.timer_count // 60
        seconds = self.timer_count % 60
        self.timer_var.set(f'{minutes:02d}:{seconds:02d}')
        if self.timer_running:
            self.root.after(1000, self.start_timer)

    def change_difficulty(self, difficulty):
        self.current_difficulty = difficulty

    def show_best_time(self):
        messagebox.showinfo("Лучшее время", f"Лучшее время для {self.current_difficulty} уровня сложности: {self.best_time[self.current_difficulty]}")

    def save_best_time(self):
        current_time = self.timer_count
        if current_time < self.best_time[self.current_difficulty]:
            self.best_time[self.current_difficulty] = current_time

root = tk.Tk()
game = SudokuGame(root)
root.mainloop()
