# BEGIN (write your solution here)
def fib(n):
    if n == 1:
        return 1
    elif(n >= 2):
        return fib(n - 1) + fib(n - 2)
    else:
        return 0
# END

print(fib(7))