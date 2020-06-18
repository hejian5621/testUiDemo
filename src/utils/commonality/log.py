# -*- coding: utf-8 -*-
import logging, os,sys

from os.path import path


class Log:
    """
    生成日志方法
    """

    def __init__(self, clean = False):
        # 创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        file_path = path.path()
        catalogue = file_path+"/log.txt"
        formatter = logging.Formatter('[%(asctime)s] %(pathname)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        if clean:
            if os.path.isfile(catalogue):
                with open(catalogue, 'w') as f:
                    pass
        fh = logging.FileHandler(catalogue)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        # ch = logging.StreamHandler()
        # ch.setLevel(logging.NOTSET)
        # ch.setFormatter(formatter)
        # self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def log(self, *args):
        s = ''
        for i in args:
            s += (str(i) + ' ')
        logging.debug(s)
log = Log(True)





class Logger(object):

    def __init__(self, filename='default.log', stream=sys.stdout):
        self.terminal = stream
        self.log = open(filename, 'wb+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass

# from utils.log.log import Logger
# sys.stdout = Logger('D:/python demo/a.log', sys.stdout)
# # sys.stderr = Logger('a.log_file', sys.stderr)
# print('print something')
# print('print something2')