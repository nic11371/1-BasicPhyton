import os

def write_and_read(text):
    current_dir = os.getcwd()
    file_path = os.path.join(os.path.relpath(current_dir), 'tmp/my_file.txt')
    open(file_path, 'a', encoding="utf8").writelines(["\n", text])
    return open(file_path, 'r', encoding="utf8").read()

while text := input():
    write_and_read(text)

print(write_and_read(text))