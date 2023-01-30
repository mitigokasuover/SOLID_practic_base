import sys
import time


class Logger:
    def __init__(self):
        self.prefix = time.strftime('%Y-%b-%d %H:%M:%S', time.localtime()) 

    def log(self, message):
        sys.stderr.write(f"{self.prefix} --> {message}\n")


class customer_logger(Logger):
    def __init__(self):
        super().__init__()
        self.prefix = time.strftime('%Y-%b-%d', time.localtime())
    

Logger = Logger()
Logger.log("Error happened")

C_Logger = customer_logger()
C_Logger.log("custom log message!")