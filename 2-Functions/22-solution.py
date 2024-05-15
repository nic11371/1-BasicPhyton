from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    arr_keys = []
    for k, v in sorted(d.items(), key = lambda x: x[1], reverse=True):
        arr_keys.append(k)
    return arr_keys
code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# d = {0:1, 1:2, 2:3, 3:4, 4:5}
# print(make_most_common_keys(d))

# d =  {5:3, 3:5, 0:2, 4:6, 7:10}
# print(make_most_common_keys(d))