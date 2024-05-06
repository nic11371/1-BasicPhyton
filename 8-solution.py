n = int(input())
s = []
maxA = []
for i in range(n):
    a = list(map(int, input().split()))
    s.append(a)
for j in s:
    maxA = max(j)
print(maxA)
# print(b)