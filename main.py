with open ('1.py', 'r') as f:
  lines_1 = f.readlines()

with open ('2.py', 'r') as f:
  lines_2 = f.readlines()

with open ('3.py', 'r') as f:
  lines_3 = f.readlines()
  
list_1 = []
list_1 += lines_1, lines_2, lines_3

list_sort = sorted(list_1, key=len)

with open ('new.py', 'w') as f:
  f.write(str(list_sort))