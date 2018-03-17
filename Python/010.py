i = 2
list = [2]
while (i < 2000000):
  for x in list:
    if (i % x == 0):
      break
    if (i < x * x):
      list.append(i)
      break
  i += (1 if i % 2 == 0 else 2)

print (sum(list))
