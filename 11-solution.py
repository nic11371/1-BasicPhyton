var = input().lower().split()
punc = '!,.?;:#$%^&*()'
arr_no_punc = []
arr = []
uniq_words = {}
for i in var:
    str = ""
    for j in i:
        if j not in punc:
           str += j
    arr_no_punc.append(str)
for i in arr_no_punc:
       setarr = set(i)
       counter = arr_no_punc.count(i)
       if len(i) >= 5 and counter > 2 and len(set(i)) >= 4:
              arr.append(i)
uniq_words = set(arr)
uniq = list(uniq_words)
uniq.sort()
print("\n".join(uniq))

# arr_no_punc = ["".join(j for j in i if j not in punc)
#        for i in var]