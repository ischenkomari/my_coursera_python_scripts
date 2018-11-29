
class FileReader():

    def __init__(self, file_name):
        self.name = file_name

    def read(self):
        inner_file = ""
        try:
            with open(self.name) as f:
                inner_file = str(f.read())
        except IOError as err:
            print(err)
        return inner_file

reader = FileReader("example1.txt")
print(reader.read())
