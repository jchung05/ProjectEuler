max = 0
for i in xrange(100,1000):
  for j in xrange(100, 1000):
    num = str(i * j)
    rev = num[::-1]
    if (len(num) is 6 and num[:3] == rev[:3] and i * j > max):
      max = i * j

print(max)
