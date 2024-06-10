def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN (write your solution here)
def find_second_index(value, items):
    cursor = iter(items)
    for i in cursor:
        find_index(value, cursor)
    return find_index(value, cursor)

# END

print(find_second_index('b', 'bob'))

