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
        self.guess_entry.bind("<Return>", self.chech_guess)
        # Кнопка перевірки
        self.guess_button = tk.Button(self.master, text="Перевірити",
                                      command=self.chech_guess)
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
        pass

    def chech_guess(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()
