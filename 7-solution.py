lists = input().split()
print(round((sum(len(i) for i in lists) / len(lists)), 2))
