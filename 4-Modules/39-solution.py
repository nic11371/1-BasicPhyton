import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    dates_int = [datetime.datetime.strptime(d, '%Y-%m-%dT%H:%M:%S').month for d in dates]
    return [f for f in dict(Counter(dates_int).most_common(n))]


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)

# dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59", "2023-03-01T23:59:59"]
# print(most_common_months(dates, 2))
