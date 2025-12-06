import ctypes
from game import Game

def set_dpi_awarness():
    ctypes.windll.user32.SetProcessDPIAware()

def main():
    set_dpi_awarness()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()

