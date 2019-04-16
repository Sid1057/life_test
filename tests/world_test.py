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
                Cell(0, 0, 'A'),
                Cell(1, 0, 'A'),
                Cell(0, 1, 'A'),
                Cell(1, 1, 'A'),
            })

        init_cells = world.get_cells()
        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(init_cells, result_cells)

    def test_world_line(self):
        'Test case of alived line 3x1 of cell in the game'
        horizontal_line = {
                Cell(-1, 1, 'C'),
                Cell(0, 1, 'C'),
                Cell(1, 1, 'C'),
            }
        vertical_line = {
                Cell(0, 0, 'C'),
                Cell(0, 1, 'C'),
                Cell(0, 2, 'C'),
            }
        world = World(
            vertical_line)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(horizontal_line, result_cells)
        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(vertical_line, result_cells)

    def test_world_A_cell_alone(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'A'),
            }
        empty_world = World({
            }).get_cells()
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(empty_world, result_cells)

    def test_world_B_cell_alone(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'B'),
            }
        empty_world = World({
            }).get_cells()
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(empty_world, result_cells)

    def test_world_C_cell_alone(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'C'),
            }
        empty_world = World({
            }).get_cells()
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(empty_world, result_cells)

    def test_world_D_cell_alone(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'D'),
            }
        empty_world = World({
            }).get_cells()
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(empty_world, result_cells)

    def test_world_with_all_cells(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'A'),
                Cell(1, 0, 'B'),
                Cell(2, 0, 'C'),
                Cell(3, 0, 'D'),
                Cell(4, 0, 'None'),

                Cell(1, 1, 'A'),
                Cell(2, 1, 'B'),
                Cell(3, 1, 'C'),
                Cell(4, 1, 'D'),
                Cell(5, 1, 'None'),

                Cell(2, 2, 'A'),
                Cell(3, 2, 'B'),
                Cell(4, 2, 'C'),
                Cell(5, 2, 'D'),
                Cell(6, 2, 'None'),

                Cell(3, 3, 'A'),
                Cell(4, 3, 'B'),
                Cell(5, 3, 'C'),
                Cell(6, 3, 'D'),
                Cell(7, 3, 'None'),
            }
        excpected_result = {
            Cell(1, 1, 'A'),
            Cell(2, 1, 'B'),
            Cell(2, 2, 'A'),
            Cell(3, 0, 'D'),
            Cell(3, 1, 'C'),
            Cell(3, 2, 'B'),
            Cell(4, 1, 'D'),
            Cell(4, 2, 'C'),
            Cell(5, 2, 'D'),
            }
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(excpected_result, result_cells)

    def test_square_A(self):
        before = {
                Cell(0, 0, 'A'),
                Cell(1, 0, 'A'),
                Cell(1, 1, 'A'),
                Cell(0, 1, 'A'),
            }
        excpected_result = before
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(excpected_result, result_cells)
        
    def test_square_B(self):
        before = {
                Cell(0, 0, 'B'),
                Cell(1, 0, 'B'),
                Cell(1, 1, 'B'),
                Cell(0, 1, 'B'),
            }
        excpected_result = before
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(excpected_result, result_cells)
        
    def test_square_C(self):
        before = {
                Cell(0, 0, 'C'),
                Cell(1, 0, 'C'),
                Cell(1, 1, 'C'),
                Cell(0, 1, 'C'),
            }
        excpected_result = before
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(excpected_result, result_cells)
        
    def test_square_D(self):
        before = {
                Cell(0, 0, 'D'),
                Cell(1, 0, 'D'),
                Cell(1, 1, 'D'),
                Cell(0, 1, 'D'),
            }
        excpected_result = before
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(excpected_result, result_cells)
        

    def test_world_D_cell_with_unknown(self):
        'Test case of alived line 3x1 of cell in the game'
        before = {
                Cell(0, 0, 'D'),
                Cell(0, 1, 'None'),
            }
        empty_world = World({
            }).get_cells()
        world = World(
            before)

        world.next_state()

        result_cells = world.get_cells()
        self.assertEqual(empty_world, result_cells)

    def test_set_cells(self):
        world = World({})
        cells = {Cell(0, 0, 'A')}
        world.set_cells(cells)
        self.assertEqual(cells, world.get_cells())
