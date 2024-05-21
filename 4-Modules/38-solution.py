import datetime

string_datetime = input()

def parse_time(s):
    dt_from_string = datetime.datetime.strptime(s, '%Y %m %d %H %M %S')
    delta = datetime.timedelta(days = 1)
    result = dt_from_string + delta
    return result.day


print(parse_time(string_datetime))