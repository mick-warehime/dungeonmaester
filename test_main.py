import unittest

import main


class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_stupid(self):
        exp = "hello warld"
        act = main.stupid()
        self.assertEqual(exp, act, "expected: %s, actual: %s" % (exp, act))

    def test_dumb(self):
        myname = "abc"
        expected_name = "abc"
        self.assertEqual(expected_name, myname, "expected: %s, actual: %s" % (expected_name, myname))
