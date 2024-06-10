items = [1, 2]
def duplicate(l):
    print(id(l))
    l *= 2


print(id(duplicate(items)))

print(items)