import unittest
import dm_logging as dmlog

class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_dumb(self):
        myname = "abc"
        expected_name = "abc"
        print dmlog.LOGGING_DIRECTORY
        self.assertEqual(expected_name, myname, "expected: %s, actual: %s" % (expected_name, myname))
