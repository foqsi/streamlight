# indicator.py
import tkinter as tk

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


class IndicatorGrid:
    def __init__(self, root, button_labels, key_assignments):
        self.indicators = {}
        font_size = 13
        button_width = 10
        button_height = 5
        wrap_length = 80

        for idx, label in enumerate(button_labels):
            row = idx // 4 + 1
            col = idx % 4
            self.indicators[key_assignments[idx]] = Indicator(
                root, row, col, label, wrap_length, font_size, button_width, button_height
            )

    def toggle_indicator(self, key):
        if key.lower() in self.indicators:
            self.indicators[key.lower()].toggle_color()
