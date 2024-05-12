def avg(str):
    numbers = []
    arr = str.split()
    summary = 0
    for i in arr:
        numbers.append(float(i))
    for j in numbers:
        summary += j
    result = summary / len(numbers)
    return result


lst = []
while True:
    var = input()
    if var == "" or var.isalpha():
        break
    lst.append(var)
for e in lst:
    print(avg(e))
