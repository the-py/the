from the import the
from os import path

def basename(self, other):
    self._check(path.basename(self.obj) == other,
                "Basename of {} is not {}.".format(self.obj, other))

def dirname(self, other):
    self._check(path.dirname(self.obj) == other,
                "Dirname of {} is not {}.".format(self.obj, other))

def extname(self, other):
    self._check(path.splitext(self.obj)[1] == other,
                "Extname of {} is not {}.".format(self.obj, other))

def file(self):
    self._check(path.isfile(self.obj), self.obj + "{} is not a file")

def dir(self):
    self._check(path.isdir(self.obj), self.obj + "{} is not a directory")

def link(self):
    self._check(path.islink(self.obj), self.obj + "{} is not a link")

API = [basename, dirname, extname,
       file, dir, link]

the.use(API)

# p = "/usr/name/file.ext"
# print path.basename(p)
# print path.dirname(p)
# the(p).should.have.basename("file.ext")
# the(p).should.have.dirname("/usr/name")
# p = "./the_file.py"
# the(p).should.a.file
