start = int(input())
end = int(input())
valid = True

while True:
    data = input()
    if data == "":
        break
    valid = valid & start <= int(data) <= end
print(valid)
