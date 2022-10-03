# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import arcade
from GameWindow import GameWindow


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = GameWindow(1280, 680, "אסף")
    game.setup()
    arcade.run()


