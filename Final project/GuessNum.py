import tkinter as tk
from tkinter import messagebox
import random


class GuessNum:
    def __init__(self, window):
        self.window = window
        self.window.title("Гра вгадай число")
        self.window.geometry("850x600")
        self.window.resizable(width=False, height=False)

        title = tk.Label(self.window, text="Гра 'Вгадай число'", font=("Arial", 25))
        title.pack(pady=20)

        self.min_num_label = tk.Label(self.window, text="Мінімальне число:", font=("Arial", 16),)
        self.min_num_label.pack(side="top", padx=5, pady=5)
        self.min_num_ask = tk.Entry(self.window)
        self.min_num_ask.pack(side="top", padx=5, pady=5)

        self.max_num_label = tk.Label(self.window, text="Максимальне число:", font=("Arial", 16))
        self.max_num_label.pack(side="top", padx=5, pady=5)
        self.max_num_ask = tk.Entry(self.window)
        self.max_num_ask.pack(side="top", padx=5, pady=5)

        self.attempts_label = tk.Label(self.window, text="Спроби:", font=("Arial", 16))
        self.attempts_label.pack(side="top", padx=5, pady=5)
        self.attempts_ask_num = tk.Entry(self.window)
        self.attempts_ask_num.pack(side="top", padx=5, pady=5)

        self.start_button = tk.Button(self.window, text="Почати гру", command=self.start_game, height=3, width=9, font=("Arial", 25))
        self.start_button.pack(pady=35, side="bottom")

        self.guess_label = tk.Label(self.window, text="Вгадай число", font=("Arial", 16))

        self.guess_entry = tk.Entry(self.window, font=("Arial", 25))

        self.submit_button = tk.Button(self.window, text="Вгадати", command=self.check_guess, height=3, width=9, font=("Arial", 25), )

        self.secret_num = None
        self.remaining_attempts = None

    def start_game(self):
        try:
            min_num = int(self.min_num_ask.get())
            max_num = int(self.max_num_ask.get())
            self.secret_num = random.randint(min_num, max_num)
            self.remaining_attempts = int(self.attempts_ask_num.get())

            self.max_num_label.destroy()
            self.min_num_label.destroy()
            self.max_num_ask.destroy()
            self.min_num_ask.destroy()
            self.attempts_ask_num.destroy()
            self.start_button.destroy()

            self.attempts_label.destroy()

            self.guess_label.pack()

            self.guess_entry.pack()

            self.submit_button.pack(pady=35)

        except ValueError:
            messagebox.showinfo("Помилка данних", "Ви ввели некоректні дані")

    def check_guess(self):
        guess = int(self.guess_entry.get())

        if guess == self.secret_num:
            messagebox.showinfo("Вітаємо!", "Ви вгадали число!")
            self.window.destroy()
            return

        self.remaining_attempts -= 1
        if self.remaining_attempts == 0:
            messagebox.showinfo("Кінець гри", f"Ви не вгадали число. Загадане число було {self.secret_num}.")
            self.window.destroy()
        elif guess < self.secret_num:
            messagebox.showinfo("Спробуйте ще раз", "Спробуйте більше число.")
        else:
            messagebox.showinfo("Спробуйте ще раз", "Спробуйте менше число.")


def main():
    root = tk.Tk()
    app = GuessNum(root)
    root.mainloop()


if __name__ == "__main__":
    main()
