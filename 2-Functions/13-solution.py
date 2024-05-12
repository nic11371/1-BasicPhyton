def transformation(str):
    str_no_punc = ""
    str = str.lower()
    if str[0] == "!":
        str = str.upper()
    for i in str:
        if i not in punc:
            str_no_punc += i
    return str_no_punc


punc = '!@#%'
lst = []
while True:
    var = input()
    if var == "":
        break
    lst.append(var)
for i in lst:
    print(transformation(i))
