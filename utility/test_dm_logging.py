import unittest
import dm_logging
import re

# standard pattern for including logger in other files
module_name = 'test_dm_logging'
logger = dm_logging.getLogger(module_name)


class MainTestCase(unittest.TestCase):
    # not sure what order tests execute in - instead of counting lines
    # just see if log contains content anywhere
    def log_contains_content(self, content):
        # content = (module name, level, msg)
        log = open(dm_logging.LOGFILE)

        ptrn = r'^\d{2}-\d{2}-\d{4} \d{2}:\d{2}\s+%s\s+%s\s+%s' % content
        content_found = any(filter(lambda x: re.search(ptrn, x), log.read().split('\n')))
        log.close()

        return content_found

    def test_log_initialization_via_import(self):
        content = ('root', 'INFO', 'BEGIN RUNTIME LOG')
        initialized_log = self.log_contains_content(content)
        self.assertTrue(initialized_log, 'unexpected format for first line of log')

    def test_warning_log(self):
        warning = 'moving my logfiles!'
        logger.warn(warning)

        content = (module_name, 'WARNING', warning)
        logged_warning = self.log_contains_content(content)
        self.assertTrue(logged_warning, 'warning was not logged to file properly')

    def test_info_log(self):
        info = 'nothing to see here'
        logger.info(info)

        content = (module_name, 'INFO', info)
        logged_info = self.log_contains_content(content)
        self.assertTrue(logged_info, 'info was not logged to file properly')

    def test_error_log(self):
        # prints to std out too!
        error = 'nothing to see here'
        logger.error(error)

        content = (module_name, 'ERROR', error)
        logged_info = self.log_contains_content(content)
        self.assertTrue(logged_info, 'info was not logged to file properly')
