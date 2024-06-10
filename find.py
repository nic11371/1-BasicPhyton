def find_index(value, items):
    for index, item in enumerate(items):
        if item == value:
            return index


# BEGIN (write your solution here)
def find_second_index(value, items):
    first_index = find_index(value, items)
    second_index = None
    if first_index is None:
        return None
    for i in range(first_index + 1, len(items)):
        if items[i] == value:
            second_index = i
            break
    return second_index

# END
print(find_second_index('n', 'cannon'))