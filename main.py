# main.py
import tkinter as tk
import threading
from keyboard_listener import KeyboardListener
from indicator import IndicatorGrid

# Button labels and their corresponding key assignments
button_labels = [
    "Tiktok Mic",  "Cat Cam",               "Desktop Audio",    "OBS Recording",
    "Discord Mic", "Discord Share Screen",  "Monitor Display",  "",
    "OBS Mic",     "Face Cam",              "BRB",              ""
]
key_assignments = [
    "f13", "f14", "f15", "f16",
    "f17", "f18", "f19", "f20",
    "f21", "f22", "f23", "f24"
]

# Setup the main window
root = tk.Tk()
root.title("StreamLights")

# Create the indicator grid and add indicators to the window
indicators = IndicatorGrid(root, button_labels, key_assignments)

# Automatically adjust the window size to fit the blocks
root.update_idletasks()
root.geometry(f"{root.winfo_width()}x{root.winfo_height()}")
root.pack_propagate(False)

# Start the keyboard listener in a separate thread
listener_thread = threading.Thread(target=KeyboardListener(key_assignments, indicators).start, daemon=True)
listener_thread.start()

# Run the Tkinter main loop
root.mainloop()
