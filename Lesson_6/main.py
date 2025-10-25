import random                   # випадкові числа
import tkinter as tk            # вікно програми
from tkinter import messagebox  # вікно повідомлень

class GuessingGame:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.master.title("Гра: Вгадай число")
        self._build_widgets()
        self.reset_game()
    
    def _build_widgets(self):
        self.info_label = tk.Label( # Текстовий віджет
            self.master,
            text="Комп'ютер загадав число від 1 до 100. Спробуй вгадати:")
        self.info_label.pack(padx=12, pady=(12, 8)) # Зовнішні відступи віджета

        entry_frame = tk.Frame(self.master)
        entry_frame.pack(padx=12, pady=4)

        tk.Label(entry_frame, text="Ваша спроба: ").pack(side=tk.LEFT)

        self.guess_entry = tk.Entry(entry_frame, width=10, justify="center")
        self.guess_entry.pack(side=tk.LEFT, padx=(6,0))
        self.guess_entry.bind("<Return>", self.check_guess)
        # Кнопка перевірки
        self.guess_button = tk.Button(self.master, text="Перевірити",
                                      command=self.check_guess)
        self.guess_button.pack(padx=12, pady=(4, 8))
        # текст підказка
        self.feedback_label = tk.Label(self.master,
            text="Введіть число вище і натисніть кнопку.")
        self.feedback_label.pack(padx=12, pady=(4, 8))
        # текст - кількість спроб
        self.attempts_label = tk.Label(self.master, text="Спроб: 0")
        self.attempts_label.pack(padx=12, pady=(0, 12))
        # Кнопка "Нова гра", або перезапуск
        self.reset_button = tk.Button(self.master, text="Нова гра",
            command=self.reset_game)
        self.reset_button.pack(padx=12, pady=(4, 8))

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.feedback_label.config(text="Нова гра! Число вже загадано.")
        self.attempts_label.config(text="Спроб: 0")
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.focus_set()

    def check_guess(self):
        guess_value = self.guess_entry.get().strip()
        if not guess_value.isdigit():
            self.feedback_label.config(text="Будь ласка, вводьте лише цілі числа.")
            self.guess_entry.select_range(0, tk.END)
            self.guess_entry.focus_set()
            return
        
        guess = int(guess_value)
        if not 1 <= guess <= 100:
            self.feedback_label.config(text="Число має бути в межах від 1 до 100.")
            self.guess_entry.select_range(0, tk.END)
            self.guess_entry.focus_set()

        self.attempts += 1
        self.attempts_label.config(text=f"Спроб: {self.attempts}")

        if guess == self.secret_number:
            messagebox.showinfo("Перемога",
                f"Вітаємо! Ви відгадали число за {self.attempts} спроб.")
            self.reset_game()
        elif guess < self.secret_number:
            self.feedback_label.config(text="Загадане число більше.")
        else: 
            self.feedback_label.config(text="Загадане число менше.")
        
        


if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()
