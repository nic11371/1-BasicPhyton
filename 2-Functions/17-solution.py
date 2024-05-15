def my_filter(func, seq):
    arr = []
    for i in seq:
        if func(i):
            yield i


func_in, seq_in = eval(input()), eval(input())

for x in my_filter(func_in, seq_in):
    print(x)

# Function filter

# a = filter(lambda x: x < 0, (1, 6, 0, 7, -1, -2, 5))
#
# for x in a:
#     print(x)

# Function without yield

# def my_filter(func, seq):
#     arr = []
#     for i in seq:
#         if func(i):
#             arr.append(i)
#     return arr
#
#
# func_in, seq_in = lambda x: x < 0, eval(input())
#
# for x in my_filter(func_in, seq_in):
#     print(x)