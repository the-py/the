# -*- coding: utf-8 -*-
from termcolor import cprint, colored
from sys import stdout

class Default:
    def before(self, world):
        print("\n" * 2)
        stdout.write(" " * 10)
        stdout.flush()

    def after(self, errors):
        self.__summary(errors)
        index = 0
        for err in errors:
            if err[-1]:
                index += 1
                cprint("  {}). ".format(index) + " ".join(err[0]), "red")
                message = err[-1].pop()
                cprint("    " + message)
                cprint(" => " + err[-1][0], "cyan", end='')
                cprint("    ".join(err[-1][1:]), "grey")

    def ok(self, the):
        stdout.write(colored(' ¶', 'green'))
        stdout.flush()

    def fail(self, tarce, the):
        stdout.write(colored(' ¶', 'red'))
        stdout.flush()

    def __summary(self, errors):
        print("\n")
        total = len(errors)
        passed = len(filter(lambda x: not x[-1], errors))
        failed = total - passed
        print("    Passed: {}/{}.  Failed: {}/{}".format(passed, total, failed, total))
        print("\n" * 2)
