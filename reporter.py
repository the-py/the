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
            if err[1]:
                index += 1
                cprint("  {}). ".format(index) +
                       " ".join(map(lambda x: str(x.message), err[0])), "red")
                message = err[1].pop()
                print("    " + message)
                cprint("    ".join([''] + err[1]), "grey")

    def ok(self, the):
        stdout.write(colored(' .', 'green'))
        stdout.flush()

    def fail(self, tarce, the):
        stdout.write(colored(' .', 'red'))
        stdout.flush()

    def __summary(self, errors):
        print("\n")
        total = len(errors)
        passed = len(filter(lambda x: x[1], errors))
        print("    Passed: {}/{}.  Failed: {}/{}".format(passed, total, total-passed, total))
        print("\n" * 3)
