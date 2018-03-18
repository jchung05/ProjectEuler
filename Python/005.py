i = 2520
while (i < 999999999):
  x = 1
  for j in xrange(1, 21):
    if (i % j != 0):
      x = 0
      break
  if (x == 1):
    print(i)
    break
  i += 2520
