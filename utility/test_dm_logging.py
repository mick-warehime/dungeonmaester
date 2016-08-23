import unittest
import dm_logging


class MainTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_log(self):
        logger = dm_logging.getLogger('LOG TEST')
        logger.error('done doing something')
        print dm_logging.LOGFILE
        self.assertEqual(1, 1, "expected: %s, actual: %s" % (1, 1))
