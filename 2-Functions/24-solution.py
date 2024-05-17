def cache_deco(func):
    cache = {}
    def wrapper(x):
        if x in cache.keys():
            return cache.get(x)
        else:
            a = func(x)
            cache[x] = a
            return a

    return wrapper

def solution(func_map, func_filter, data):
    list_filter = []
    for f in data:
        if func_filter(f):
            list_filter.append(f)
    for i, m in enumerate(list_filter):
        if i % 2 == 0:
            yield func_map(m)
        else: func_map(m)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)