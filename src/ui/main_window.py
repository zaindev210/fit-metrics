import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self, root):
        self.root = root

        self.root.title("FitMetrics")
        self.root.geometry("900x600")
        self.root.minsize(700, 500)

        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(
            self.root,
            text="FitMetrics",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)

        subtitle = ttk.Label(
            self.root,
            text="Fitness & Health Assessment",
            font=("Arial", 14)
        )
        subtitle.pack()

