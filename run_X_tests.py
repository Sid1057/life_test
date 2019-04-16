#!/usr/bin/python3

from tests.gui_test import Test_gui
from tests.app_test import Test_app
import unittest

suite = unittest.TestLoader().loadTestsFromTestCase(Test_gui)
unittest.TextTestRunner(verbosity=2).run(suite)

suite = unittest.TestLoader().loadTestsFromTestCase(Test_app)
unittest.TextTestRunner(verbosity=2).run(suite)
