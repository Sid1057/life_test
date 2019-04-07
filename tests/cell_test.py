from modules.cell import Cell

import unittest


class Test_cell(unittest.TestCase):
    'Class for testing cell methods.'
    def test_cell_get_coords(self):
        'Test if cell could return correct coordinates'
        zero_cell = Cell(0, 0)

        self.assertEqual(zero_cell.get_coords(), (0, 0))

    def test_cell_magic(self):
        'Test if magic methods works correctly'
        zero_cell = Cell(0, 0)
        another_zero_cell = Cell(0, 0)
        non_zero_cell = Cell(0, 10)
        another_non_zero_cell = Cell(10, 0)

        self.assertEqual(zero_cell, another_zero_cell)
        self.assertNotEqual(zero_cell, non_zero_cell)
        self.assertNotEqual(zero_cell, another_non_zero_cell)
        self.assertNotEqual(another_zero_cell, non_zero_cell)
        self.assertNotEqual(another_zero_cell, another_non_zero_cell)

        self.assertEqual(set([zero_cell]), set([another_zero_cell]))
        self.assertNotEqual(set([zero_cell]), set([non_zero_cell]))

    def test_cell_get_neighbours(self):
        'Test if cell could get correct position of its neighbours'
        zero_cell = Cell(0, 0)
        self.assertEqual(len(zero_cell.get_neighbours()), 8)
        self.assertSequenceEqual(
            zero_cell.get_neighbours(),
            [Cell(i[0], i[1]) for i in (
                (-1, -1), (0, -1), (1, -1),
                (-1,  0),          (1,  0),
                (-1,  1), (0,  1), (1,  1))])
