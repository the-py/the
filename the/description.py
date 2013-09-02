from context import Context, ContextException

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

Suite = Desc = Description
