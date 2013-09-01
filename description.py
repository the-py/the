class Description(object):
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        Context().stepin(self)
        return self

    def __exit__(self):
        Context().stepout()

Suite = Desc = Description
