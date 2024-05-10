number = int(input())
array = []
maxValues = []
maxStr = []
for i in range(number):
    a = input().split()
    intValue = []
    for j in a:
        b = int(j)
        intValue.append(b)
    array.append(intValue)
for value in array:
    c = max(value)
    maxValues.append(c)
maxValues.sort()
maxValues.reverse()
for j in maxValues:
    d = str(j)
    maxStr.append(d)
print(";".join(maxStr))
