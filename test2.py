def sort_pair(tup):
    a, b = tup
    if a > b:
        return (b, a)
    else:
        return (a, b)

print(sort_pair((1, 5)))