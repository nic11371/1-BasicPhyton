var = input()
valid = True
for i in var:
  if (i == "i" or i == "e"):
     valid = False
  elif (i == "a" and i == "o"):
     valid = True
print(valid)