from collections import defaultdict
from typing import List, Tuple


def fill_specializations(specializations: List[Tuple[str, str]]):
    default_value = defaultdict(list)
    for k, v in specializations:
        default_value[k].append(v)
    return dict(default_value)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# specs = [('Sales', 'John Doe'), ('Sales', 'Martin Smith'), ('Accounting', 'Jane Doe'), ('Marketing', 'ElizabethSmith'), ('Marketing', 'Adam Doe')]
# print(fill_specializations(specs))
