import logging

class LOGHandler(object):

    def __init__(self):
        self.name = None
        self.path_file = None
        self.logger = None
        self.handler = None
        self.formatter = None

    def create_logger(self, name, path_file):
        """Create logger given a name and path file.
        Keyword argument:
        name -- name of logger
        path_file -- path for the log file
        Return:
        logger -- the logger created
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        # create a file handler
        self.handler = self.create_handler(path_file)
        # add the handlers to the logger
        self.logger.addHandler(self.handler)
        return self.logger

    def create_handler(self, path_file):
        """Create handler object given a log file and specific message format.
        Keyword argument:
        path_file -- path of the log file

        Return:
        handler -- handler object with specific file and message format
        """
         # create a file handler
        self.handler = logging.FileHandler(path_file)
        self.handler.setLevel(logging.INFO)
        #self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        self.formatter = logging.Formatter('%(asctime)-15s  %(levelname)-8s  %(message)s')
        self.handler.setFormatter(self.formatter)
        return self.handler
