import sys
import os.path
import logging
import unittest
import datetime
from ...handlers.log_handler import LOGHandler

class TestLOGHandler(unittest.TestCase):
    def test_verify_that_log_file_is_created_correctly(self):
        logger = LOGHandler()
        logger.create_logger("create_example", 'logs/create_logger_example.log')
        logger_test = logging.getLogger('create_example')
        logger_test.info("example")
        result = os.path.isfile("logs/create_logger_example.log")
        self.assertTrue(result)

    def test_verify_that_log_message_has_format_datetime_level_and_message(self):
        logger = LOGHandler()
        logger.create_logger("message_test", 'logs/message_test.log')
        logger_test = logging.getLogger('message_test')
        logger_test.warning("message_test")
        with open('logs/message_test.log', 'r') as f:
            data = f.readlines()
            first_line = data[0]
            words = first_line.split()
            date_time = words[0] + " " + words[1]
            level = words[2]
            message = words[3]
        date_type = datetime.datetime.strptime(date_time, "%Y-%m-%d %H:%M:%S,%f")
        self.assertTrue(isinstance(date_type, datetime.datetime))
        self.assertTrue(level == "WARNING")
        self.assertTrue(message == "message_test")
      
if __name__ == "__main__":
   unittest.main()
