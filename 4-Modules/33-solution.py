import os

text = input()


def write_and_read(text):
    current_dir = os.getcwd()
    file_path = os.path.join(os.path.relpath(current_dir), 'tmp/my_file.txt')
    open(file_path, 'w').write(text)
    return open(file_path, 'r').read()


print(write_and_read(text))