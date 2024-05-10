var = input()
a = set(var.lower())
s = []
for i in a:
    s.append(i)
    if i == " ":
        s.remove(i)
    s.sort()
print(" ".join(s))