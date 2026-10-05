from tkinter import *
from tkinter import ttk


#This is a part of a WIP Theme database for tkinter ttk
"""
F4F4F4 - OFFWHITE
B6B6B6 - MOON DUST
FC3D21 - NASA WORM RED
D1480F - FUEL TANK ORAANGE
A2673F - BOOSTER COPPER
1D7373 - ULA RETRO CYAN
1A1A1A - CARBON
"""
def apply_theme():
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('Frame',
                background= '#F4F4F4'
                )
    style.configure('TLabel',
                    font =('Arial', 12),
                    padding=10,
                    background= '#F4F4F4',
                    foreground= '#1A1A1A')
    style.configure('TButton',
                font =('Arial', 12),
                pady=10,
                padx=10,
                background='#1d7373')
    style.configure('TEntry',
                    font=('Arial', 12),
                    padding=10,
                    background= '#F4F4F4',
                    foreground='#1A1A1A',
                    border= '#F4F4F4')
    return style
