from termcolor import cprint

class Default:
    def before(self, world):
        print "\n" * 2

    def after(self, errors):
        print "\n" * 3
        for err in errors:
            if err[1]:
                cprint("---- " + "->".join(map(lambda x: str(x.message), err[0])) + " ----", "red")
                cprint("".join(err[1]), "grey")

    def ok(self, error):
        cprint('.', 'green', end='')

    def fail(self, error):
        cprint('.', 'red', end='')

    def __summary(self):
        pass
