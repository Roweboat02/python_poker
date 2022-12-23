import tkinter as tk
from enum import Enum


class AdvanceButton():
    callback = None
    def __init__(self, frame):
        self.button = tk.Button(frame, text="Advance", command=self.call_callback)
        self.button.grid(column=1, row=0)

    def call_callback(self):
        self.callback()
