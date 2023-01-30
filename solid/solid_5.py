import sys
import time


class TerminalPrinter:
    def write(self, msg):
        sys.stderr.write(f"{msg}\n")
    

class FilePrinter:
    def write(self, msg):
        with open("log.txt", "a+", encoding="UNF8") as f:
            f.write(f"{msg}\n")


class Logger:
    def __init__(self):
        self.prefix = time.strftime("%Y-%b-%d %H:%H:%S", time.localtime())
    

    def log_stderr(self, message):
        TerminalPrinter().write(f"{self.prefix} {message}")
    

    def log_file(self, message):
        FilePrinter().write(f"{self.prefix} {message}")


Logger = Logger()
Logger.log_file("starting the program....")
Logger.log_stderr("An error")