import datetime

days, seconds = int(input()), int(input())

def shift_time(days: int, seconds: int):
    delta = datetime.timedelta(days = days, seconds = seconds)
    current = datetime.datetime(2023, 1,1, 12, 30, 0)
    result = current + delta
    return (result.day, result.second)

print(shift_time(days, seconds))