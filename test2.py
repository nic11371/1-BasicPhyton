<<<<<<< HEAD
def sort_pair(tup):
    a, b = tup
    if a > b:
        return (b, a)
    else:
        return (a, b)

print(sort_pair((1, 5)))
=======
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
>>>>>>> 940b28f81c52d5c1263402425a7c23356a2d6172
