import time
import logging

class LogOutput():
    def logOutput(self, log_dir, name_project):
        now = time.strptime('%Y-%m-%d %H:%M:S')
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_dir + now + '-' + name_project + '_test_log.log',
                            filemode='w')
        logger = logging.getLogger()
        logger.info(self)