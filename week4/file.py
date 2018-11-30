import os.path
import tempfile

class File:
    def __init__(self, name):
        self.name = name
        self.file_end = 0
        self.obj = []
        f = open(self.name, 'w')
        f.close()

    def __str__(self):
        return self.name

    def __getitem__(self, index):
        with open(self.name) as file:
            self.obj = file.readlines()
        return self.obj[index]

    def __add__(self, object):
        new_file_name = "{}{}".format(os.path.basename(self.name), os.path.basename(object.name))
        new_file_path = str(os.path.join(tempfile.gettempdir(), new_file_name))
        parent_files_list = [self, object]
        for i in parent_files_list:
            with open(i.name) as file:
                content = "".join(file.read())
        with open(new_file_path, 'w') as file:
            file.write(content)
            print(new_file_path)

    def len(self):
        with open(self.name) as file:
            self.file_end = sum(1 for line in file)
        return self.file_end

    def write(self, content):
        with open(self.name, 'w') as file:
            file.write(content)

def _main():
    obj = File('file.txt')
    obj.write('lineasdas\nkfnldkldfk\ndfgdfgdsf\n')
    first = File('first')
    first.write("kjhdfkjshdfkjh\nlkjlkjlj\nkfjdflkflhflghk")
    second = File('second')
    second.write("ur894398y23784634789\nkjhdfkjshdfkjh\nlkjlkjlj\nkfjdflkflhflghk")
    new_obj = first + second
    for line in obj:
        print(line)

if __name__ == "__main__":
    _main()
