import tkinter as tk
from pynput import keyboard
import threading

class Indicator:
    def __init__(self, parent, row, col, label, wrap_length, font_size, button_width, button_height):
        self.current_color = "green"
        self.indicator = tk.Label(
            parent,
            text=label,
            bg=self.current_color,
            fg="white",
            font=("Arial", font_size),
            width=button_width,
            height=button_height,
            wraplength=wrap_length,
            relief="solid"
        )
        self.indicator.grid(row=row, column=col, padx=2, pady=2)

    def toggle_color(self):
        self.current_color = "red" if self.current_color == "green" else "green"
        self.indicator.config(bg=self.current_color)

button_labels = [
    "Tiktok Mic",   "Cat Cam",                  "Desktop Audio",    "OBS Recording",
    "Discord Mic",  "Discord Share Screen",     "Monitor Display",  "",
    "OBS Mic",      "Face Cam",                 "BRB",              "",
]  # Labels for each button
font_size = 13           # Font size for button text
button_width = 10        # Button width in characters
button_height = 5        # Button height in lines
wrap_length = 80         # Maximum width for wrapping text (in pixels)
key_assignments = [      # Keys that toggle buttons
    "f13", "f14", "f15", "f16",
    "f17", "f18", "f19", "f20",
    "f21", "f22", "f23", "f24"
]

# Setup the main window
root = tk.Tk()
root.title("Macro Grid")

indicators = {}
for idx, label in enumerate(button_labels):
    row = idx // 4 + 1
    col = idx % 4
    indicators[key_assignments[idx]] = Indicator(
        root, row, col, label, wrap_length, font_size, button_width, button_height
    )

# Automatically adjust the window size to fit the blocks
root.update_idletasks()
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
root.pack_propagate(False)

def handle_keypress(key):
    try:
        if isinstance(key, keyboard.KeyCode):
            key_str = key.char
        elif isinstance(key, keyboard.Key):
            key_str = key.name
        else:
            key_str = str(key).split('.')[1]  # To get 'f13', 'f14', etc.

        if key_str.lower() in key_assignments:
            indicators[key_str.lower()].toggle_color()
    except AttributeError:
        # Handles special keys that don't have a .char attribute
        pass

# Use threading to run the keyboard listener in the background
def keyboard_listener():
    with keyboard.Listener(on_press=handle_keypress) as listener:
        listener.join()

# Start the keyboard listener in a separate thread
listener_thread = threading.Thread(target=keyboard_listener, daemon=True)
listener_thread.start()

# Run the Tkinter main loop
root.mainloop()
