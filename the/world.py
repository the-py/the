from context import Context
from copy import copy
from reporter import Default

class World(object):
    __instance = None

    def __new__(cls, error=None, reporter = Default):
        if not cls.__instance:
            i = cls.__instance = super(World, cls).__new__(cls)
            i.message = error
            i.reporter = reporter()
            i.errors = []
        if error:
            i.add(error)
        return cls.__instance

    def __enter__(self):
        Context().reset().stepin(self)
        self.reporter.before(self)
        return self
    begin = enter = __enter__

    def __exit__(self, etype=None, evalue=None, trace=None):
        self.reporter.after(self.errors)
        self.errors = []
        Context().reset()
        return True
    done = leave = __exit__

    def add(self, error, current=None):
        chain = copy(Context().chain)
        if current and not current.as_context:
            chain.append(current)
        self.errors.append([chain, error])
    append = add

TheTest = World

# def function_in_the_world(fn, self_info=None):
#     def _fn(*args, **kwargs):
#         this = self_info or args[0]
#         try:
#             fn(*args, **kwargs)
#         except Exception as e:
#             World().reporter.fail(traceback.format_stack() + [e.message], this)
#             World().append(traceback.format_stack() + [e.message], this)
#         else:
#             World().reporter.ok(this, None)
#             World().append(None)
#     return _fn

