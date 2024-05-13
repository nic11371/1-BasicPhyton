dict = {}
def fib(n):
    if n in (1, 2):
        return 1
    if n in dict.values():
        return n

    return fib(n - 1) + fib(n - 2)


num = int(input())
if 1 <= num <= 30:
    print(fib(num))
else:
    print(-1)
print(dict)