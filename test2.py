# items = [1, 2, 3]
# def rotate(l):
#     a = l.pop()
#     l.insert(0, a)
#
# rotate(items)
# print(items)

# s = 'ABRAKADABRA'
# print(s[6:1:-1])
l = "ABCD"
a = [1, 2, 3, 4]
# def rotated_left(item):
#     return item[1:] + item[:1]
#
# print(rotated_left(l))
#
# def rotated_right(item):
#     return item[-1:] + item[:-1]
#
# print(rotated_right(a))

def find_index(value, sequence):
    for i, s in enumerate(sequence):
        if s == value:
            return i
    else: return None

print(find_index(42, [1, 2, 3, 4, 5]))