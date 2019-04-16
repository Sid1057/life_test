from modules.gui import Gui
from modules.world import World
from modules.cell import Cell
from app import Application
import tkinter as tk

import unittest


class Test_app(unittest.TestCase):
    'Class for testing gui status messages.'

    def test_widgets_creating(self):
        root = tk.Tk()
        app = Application(master=root)
        app.update_borders()
        app.mainloop()

