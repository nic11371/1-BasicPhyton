from itertools import zip_longest
from typing import List, Tuple


def fill_missing_values(values_list_1: List[int], values_list_2: List[int]) -> List[Tuple[int, int]]:
    list_values = []
    for el1, el2 in zip_longest(values_list_1, values_list_2):
        if el1 is None: el1 = 1
        if el2 is None: el2 = 1
        tuple_values = (el1, el2)
        list_values.append(tuple_values)
    return list_values


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# print(fill_missing_values([1, 2, 3], [2, 3, 4, 5]))
