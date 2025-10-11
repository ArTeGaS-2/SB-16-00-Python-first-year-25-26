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

    def reset_game(self):
        pass

    def chech_guess(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    GuessingGame(root)
    root.mainloop()
