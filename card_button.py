from typing import Tuple
import tkinter as tk
from tkinter.font import Font

class CardButton:
    RED = "#FF0000"
    BLACK = "#000000"
    HELD_WHITE = "#C8C8C8"
    WHITE = "#FFFFFF"

    face_val: str = ""
    text_color: Tuple[int]
    background_color: Tuple[int]
    held: bool = False

    def __init__(self, frame, index:int):
        self.button = tk.Button(frame,
                                text="",
                                command=self.toggle_held,
                                font=Font(size=20),
                                height=4,
                                width=5,
                                background=self.WHITE
                                )
        self.button.grid(column=index, row=0)
        self._set_background_color_from_held()

    def _set_text_color_from_face_val(self):
        if (self.face_val[0]=="\u2666" or self.face_val[0]=="\u2665" or self.face_val[0]=="D"or self.face_val[0]=="H"):
            self.button["fg"] = self.RED
        else:
            self.button["fg"] = self.BLACK

    def _set_background_color_from_held(self):
            if self.held:
                self.button["bg"] = self.HELD_WHITE
            else:
                self.button["bg"] = self.WHITE

    def set(self, text: str):
        self.face_val = text
        self.button["text"] = text
        self._set_text_color_from_face_val()

    def toggle_held(self, res=None):
        self.held = not self.held if res is None else res
        self._set_background_color_from_held()

    def update(self): pass
