max = 0
maxnum = 0
i = 999999
while (i > 1):
  tmp = i
  count = 1
  while (tmp != 1):
    if (tmp % 2 == 1):
      tmp *= 3
      tmp += 1
      count += 1
    else:
      tmp /= 2
      count += 1
  if (count > max):
    max = count
    maxnum = i
  i -= 1
    
print(maxnum)
