from the import the
from os import path as ospath

def basename(self, other):
    return self._check(ospath.basename(self.obj) == other,
                       "Basename of {} is not {}.".format(self.obj, other))

def dirname(self, other):
    return self._check(ospath.dirname(self.obj) == other,
                       "Dirname of {} is not {}.".format(self.obj, other))

def extname(self, other):
    return self._check(ospath.splitext(self.obj)[1] == other,
                       "Extname of {} is not {}.".format(self.obj, other))

def path(self):
    return self._check(ospath.exists(self.obj), self.obj + " doesn't exist.")

def file(self):
    return self._check(ospath.isfile(self.obj), self.obj + " is not a file")

def dir(self):
    return self._check(ospath.isdir(self.obj),
                       self.obj + " is not a directory")

def link(self):
    return self._check(ospath.islink(self.obj), self.obj + " is not a link")

def mount(self):
    return self._check(ospath.ismount(self.obj),
                       self.obj + " is not a mount point")

def absolute_path(self):
    return self._check(ospath.isabs(self.obj),
                       self.obj + " is not an absolute path")

API = [basename, dirname, extname, path, file, dir, link, mount, absolute_path]

# the.use(API)

# p = "/usr/name/file.ext"
# print ospath.basename(p)
# print ospath.dirname(p)
# the(p).should.have.basename("file.ext")
# the(p).should.have.dirname("/usr/name")
# p = "./the_fs.py"
# the(p).should_not.be.a.dir
# the(p).should.be.a.link
