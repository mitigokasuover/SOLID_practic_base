import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")
    

class FilePrinter:
    def write(self, msg):
        with open("log.txt", "a+", encoding="UTF8") as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime("%Y-%b-%d %H:%H:%S", time.localtime())
    

    def log(self, message, notifier):
        notifier().write(f"{self.prefix} {message}")



Logger = Logger()
Logger.log("starting the program....", TerminalPrinter)
Logger.log("An error", FilePrinter)