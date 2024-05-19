class Dictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __call__(self, *args, **kwargs):
        for k, v in self.dictionary.items():
            if k == args[0]:
                return v


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# dictionary = Dictionary({1:2, 2:1, 3:3})
# print(dictionary(2))