from tqdm import tqdm

dictionary = {}


def fib(n):
    if n in (1, 2):
        return 1
    if n in dictionary.keys():
        return dictionary.get(n)
    else:
        val = fib(n - 1) + fib(n - 2)
        dictionary[n] = val
        return val


num = int(input())
if 1 <= num <= 50:
    print(fib(num))
else:
    print(-1)
