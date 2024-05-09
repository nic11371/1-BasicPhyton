var = input().lower().split()
dictionary = {}
for i in var:
   a = var.count(i)
   dictionary.update({i: a})
max_dictionary = {}
for k, v in dictionary.items():
   max_val = max(dictionary.values())
   if v == max_val:
      max_dictionary.update({k: v})
for k, v in max_dictionary.items():
   print(k, v)
