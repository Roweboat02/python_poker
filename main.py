# Import Module
import tkinter as tk
from enum import Enum

from advance_button import AdvanceButton
from card_button import CardButton
from card_deck import random_cards
from assessor import Assess, HandToPoints
from fold_button import FoldButton


class States(Enum):
    START=0
    REPLACE=1
    ASSESS=2


# create root window
root = tk.Tk()

# root window title and dimension
root.title("Poker")
# Set geometry (widthxheight)
root.geometry('600x350')

POINTS=100
BET=0
WIN=0
HAND=[]
STATE = States.START
CARDS=[]

tk_points = tk.StringVar()
tk_points.set(f"points: {POINTS}")
tk_bet = tk.StringVar()
tk_bet.set(f"bet: {BET}")

tk_win = tk.StringVar()
tk_win.set(f"win: {WIN}")


buttons_frame = tk.Frame(root)
buttons_frame.grid(column=1, row=0)

advance_button = AdvanceButton(buttons_frame)
fold_button = FoldButton(buttons_frame)

point_frame = tk.Frame(root)

point_frame.grid(column=1, row=1)

points_label = tk.Label(point_frame, textvariable=tk_points)
bet_label = tk.Label(point_frame, textvariable=tk_bet)
win_label = tk.Label(point_frame, textvariable=tk_win)

points_label.grid(column=0, row=0)
bet_label.grid(column=1, row=0)
win_label.grid(column=2, row=0)

button_frame = tk.Frame(root)
button_frame.grid(column=1, row=2)
buttons = [CardButton(button_frame, i) for i in range(5)]

def advance():
    global CARDS
    global HAND
    global STATE
    global POINTS
    global BET
    global WIN

    if STATE==States.START:
        HAND=[]
        CARDS = random_cards()

        for i, butt in enumerate(buttons):
            HAND.append(CARDS.pop())
            butt.set(HAND[-1])
            butt.toggle_held(res=False)
        BET=0
        BET+=5
        POINTS-=5

        tk_win.set(f"win: _")
        tk_points.set(f"points: {POINTS}")
        tk_bet.set(f"bet: {BET}")

        STATE=States.REPLACE

    elif STATE==States.REPLACE:
        for i, butt in enumerate(buttons):
            if not butt.held:
                HAND[i]=CARDS.pop()
                butt.set(HAND[i])

        BET+=5
        POINTS-=5
        tk_points.set(f"points: {POINTS}")
        tk_bet.set(f"bet: {BET}")

        STATE = States.ASSESS

    elif STATE == States.ASSESS:
        WIN=HandToPoints(Assess(HAND))
        print(WIN)
        tk_win.set(f"win: {WIN}")
        POINTS+=WIN
        WIN=0
        BET=0
        STATE = States.START
advance()
advance_button.callback=advance

def fold():
    global STATE
    STATE=States.START
    advance()

fold_button.callback=fold

# all widgets will be here
# Execute Tkinter
root.mainloop()