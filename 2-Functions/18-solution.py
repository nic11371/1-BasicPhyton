def cache_deco(func):
    cache = {}

    def wrapper(*args):
        if args in cache.keys():
            return cache.get(args)
        else:
            a = func(*args)
            cache[args] = a
            return a

    return wrapper


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# def fib(k):
#     if k <= 2:
#         return 1
#     return fib(k - 1) + fib(k - 2)
#
#
# print(fib(300))