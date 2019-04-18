#!/usr/bin/python3

from tests.cell_test import Test_cell
from tests.world_test import Test_world
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(Test_cell)
unittest.TextTestRunner(verbosity=2).run(suite)

assert 1 == 2

suite = unittest.TestLoader().loadTestsFromTestCase(Test_world)
unittest.TextTestRunner(verbosity=2).run(suite)
