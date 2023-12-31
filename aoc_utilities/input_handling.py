class TxtInput:
    def __init__(self, filename):
        self.filename = filename
        self.lines = self.read()

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read().splitlines()