# keyboard_listener.py
from pynput import keyboard

class KeyboardListener:
    def __init__(self, key_assignments, indicator_grid):
        self.key_assignments = key_assignments
        self.indicator_grid = indicator_grid

    def handle_keypress(self, key):
        try:
            if isinstance(key, keyboard.KeyCode):
                key_str = key.char
            elif isinstance(key, keyboard.Key):
                key_str = key.name
            else:
                key_str = str(key).split('.')[1]  # To get 'f13', 'f14', etc.

            if key_str.lower() in self.key_assignments:
                self.indicator_grid.toggle_indicator(key_str)
        except AttributeError:
            # Handles no .char attribute
            pass

    def start(self):
        with keyboard.Listener(on_press=self.handle_keypress) as listener:
            listener.join()
