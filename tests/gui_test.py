from modules.gui import Gui
from modules.world import World
from modules.cell import Cell

import unittest


class Test_gui(unittest.TestCase):
    'Class for testing gui status messages.'

    def test_set_arggs_method(self):
        world = World()
        gui = Gui()
        gui.set_args(0, 0, 10, 10)

    def test_draw_world_in_gui(self):
        world = World({
            Cell(0, 0, 'A'),
            Cell(0, 0, 'B'),
            Cell(0, 0, 'C'),
            Cell(0, 0, 'D'),
            })
        gui = Gui()
        gui.set_args(0, 0, 10, 10)
        gui.draw(world)
