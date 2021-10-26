import tkinter as tk

class output_page:
    def __init__(self, root):
        self.root = root

        self.window = tk.Toplevel(self.root)
        self.window.title("Output")

        self.canvas = tk.Canvas(self.window, width=600, height=600)
        self.canvas.grid(columnspan=5, rowspan=10)

        self.output_label = tk.Label(self.window, text = "Insert Output Here", font = ("Raleway, 14"))
        self.output_label.grid(column = 2, row = 4)
