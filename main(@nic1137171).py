import requests


def get_online_currencies():
    host = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_JKZT111fFIEFYKheP5vyCXs5BWhNGUSqkhCChJyz&currencies=EUR%2CUSD%2CGBP%2CRUB"
    response = requests.get(host)
    return response.json().get("data")


currency = get_online_currencies()


def welcome(data):
    print("Добро пожаловать в конвертор валют!")
    print("""
Данная программа поможет вам конвертировать вашу валюту в желаемую.
- выбор исходной валюты;
- ввод количества этой валюты;
- выбор валюты конвертации.
    """)

    count = 1
    for key in data.keys():
        print(f'{count}. {key}')
        count += 1
    return count


def is_valid_string(printing):
    while True:
        enter = input(printing).upper()
        if enter not in currency:
            print("Неверный формат данных")
        else:
            break
    return enter


def conversion(current, amount, convert):
    return round(amount / currency[current] * currency[convert], 2)


def is_valid_number(printing):
    while True:
        try:
            enter = float(input(printing))
            break
        except ValueError:
            print("Неверный формат данных")
    return round(enter, 2)


welcome(currency)

print(
    f"ИТОГО: {conversion(is_valid_string("Введите имеющийся валюту: "), is_valid_number("Введите имеющуюся сумму: "), is_valid_string("Выберите валюту для конвертации: "))}")
