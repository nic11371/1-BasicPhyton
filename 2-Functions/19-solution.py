def repeat_deco(n=1):
    def deco(func):
        def wrapper(*args, **kwargs):
            count = ""
            for i in range(n):
                count = func(*args, **kwargs)
            return count

        return wrapper

    return deco


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
