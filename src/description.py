from context import Context, ContextException
from world import World
import traceback

class Description(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        Context().stepin(self)
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        Context().stepout()
        return False if etype and etype is not ContextException else True

    def __str__(self):
        return self.message

class It(object):
    def __init__(self, message, obj=None):
        self.message = message
        self.obj = obj

    def __enter__(self):
        Context().stepin(self)
        return self.obj

    def __exit__(self, etype=None, evalue=None, trace=None):
        if etype and etype is not ContextException:
            info = traceback.format_stack() + [evalue.message]
            World().reporter.fail(self, info)
            World().append(info)
        else:
            World().reporter.ok(self)
            World().append(None)
        Context().stepout()
        return True

    def __str__(self):
        return self.message
