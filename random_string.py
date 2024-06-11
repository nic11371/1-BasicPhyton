import random
def choice_from_range(string, start, stop):
    str_index = random.randint(start, stop)
    str_rand = string[str_index]
    return str_rand

text = "abcdef"
print(choice_from_range(text, 3, 5))