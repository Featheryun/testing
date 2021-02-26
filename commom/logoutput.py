import time
import logging
import datetime

class LogOutput():
    def logOutput(self, log_dir, name_project):
        now = datetime.datetime.now()
        now = time.strftime('%Y-%m-%d', time.localtime())
        logging.basicConfig(level=logging.WARNING,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            filename=log_dir + now + '-' + name_project + '_log.log',
                            filemode='w')
        logger = logging.getLogger()
        logger.info(self)


if __name__ == '__main__':
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
    print(type(datetime.datetime.now()), datetime.datetime.now())
    print(type(time.localtime()), time.localtime())
