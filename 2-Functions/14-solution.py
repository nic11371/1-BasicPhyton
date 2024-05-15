start, end, step = list(map(int, input().split()))
for i in map(lambda x: x * x if x % 2 != 0 else -x, range(start, end, step)): print(i)
