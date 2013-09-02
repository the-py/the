from context import Context

class Description(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        Context().stepin(self)
        return self

    def __exit__(self, etype=None, evalue=None, trace=None):
        Context().stepout()
        return True

Suite = Desc = Description