# def filter_string(string, char):
#     i = 0
#     result = ""
#     while i < len(string):
#         if string[i] != char:
#             result += string[i]
#         i += 1
#     return result

# def filter_string(string, char):
#     result = ""
#     for i in string:
#         if i.lower() != char.lower():
#             result += i
#     return result
#
#
# text = 'If I look back I am lost'
# print(filter_string(text, 'I'))

def print_table_of_squares(start, stop):
	for i in range(start, stop + 1):
		print(f"square of {i} is {i ** 2}")

print_table_of_squares(1, 3)
