def fact(n):
  if (n < 2):
    return (1)
  return (n * fact(n - 1))
  
i = 3
total = 0


while (i < 1000000):
  tmp = i
  sum = 0
  while (tmp != 0):
    sum += fact(tmp % 10)
    tmp //= 10
  if (sum == i):
    total += i
  i += 1

print(total)
