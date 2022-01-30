import os
import tempfile


class File:
    """
    Custom File iterator.
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.current_position = 0
        if not os.path.exists(self.filepath):
            self.write("")

    def __add__(self, other):
        new_text = self.read() + other.read()
        new_filepath = tempfile.NamedTemporaryFile().name
        new_file = File(new_filepath)
        new_file.write(new_text)
        return new_file

    def __str__(self):
        return self.filepath

    def __iter__(self):
        return open(self.filepath)

    def __next__(self):
        with open(self.filepath, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line

    def read(self):
        with open(self.filepath, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.filepath, 'w') as f:
            f.write(text)
