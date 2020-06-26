from pynput.keyboard import Controller


class Presser:
    def __init__(self):
        self.key = Controller()

    def press_letter(self, letter):
        print(f"... . . .. {letter}......")
        self.key.press(letter)
        self.key.release(letter)
