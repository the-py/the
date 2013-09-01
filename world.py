from context import Context
from copy import copy

class World(object):
    __instance = None

    def __new__(cls, error=None):
        if not cls.__instance:
            i = cls.__instance = super(World, cls).__new__(cls)
            i.message = error
            i.errors = []
        if error:
            i.add(error)
        return cls.__instance

    def __enter__(self):
        Context().reset().stepin(self)
        return self
    enter = __enter__

    def __exit__(self, etype=None, evalue=None, trace=None):
        self.out()
        self.errors = []
        Context().reset()
    leave = __exit__

    def add(self, error):
        self.errors.append([copy(Context().chain), error])
    append = add

    def out(self):
        for err in self.errors:
            print "---- " + "->".join(map(lambda x: str(x.message), err[0])) + " ----"
            if err[1]:
                print "".join(err[1])
            else:
                print "passed"
            print "=========================================================\n"


