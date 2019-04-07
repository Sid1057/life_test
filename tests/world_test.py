from modules.cell import Cell
from modules.world import World

import unittest


class Test_world(unittest.TestCase):
    'Class for testing world behaviour.'

    def test_get_set_cells(self):
        'Test if world could give set of alived cells correctly'
        world = World()
        self.assertEqual(world.get_cells(), set())

        world = World({
            Cell(0, 0),
            Cell(3, 1),
            Cell(0, 0),
            })
        self.assertEqual(
            world.get_cells(),
            {
                Cell(3, 1),
                Cell(0, 0)})

    def test_empty_world(self):
        'Test case of empty field'
        world = World(
            {
            })

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(len(result_cells), 0)

    def test_world_one_cell(self):
        'Test case of one alive cell in the game'
        world = World(
            {
                Cell(0, 0)
            })

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(len(result_cells), 0)

    def test_world_square(self):
        'Test case of square of alive cell in the game'
        world = World(
            {
                Cell(0, 0),
                Cell(1, 0),
                Cell(0, 1),
                Cell(1, 1),
            })

        init_cells = world.get_cells()
        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(init_cells, result_cells)

    def test_world_line(self):
        'Test case of alived line 3x1 of cell in the game'
        horizontal_line = {
                Cell(-1, 1),
                Cell(0, 1),
                Cell(1, 1),
            }
        vertical_line = {
                Cell(0, 0),
                Cell(0, 1),
                Cell(0, 2),
            }
        world = World(
            vertical_line)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(horizontal_line, result_cells)
        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(vertical_line, result_cells)
