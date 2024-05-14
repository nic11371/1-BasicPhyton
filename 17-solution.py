def filter(func, seq) :
    arr = []
    for i in seq:
        val = func(i)
        if val:
            arr.append(i)
    return arr
func_in, seq_in = eval(input()), eval(input())


for x in filter(func_in, seq_in):
    print(x)