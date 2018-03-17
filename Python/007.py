def is_prime(n):
  if (n < 2):
    return (0)
  
  i = 2
  while (i <= n // 2):
    if (n % i == 0):
      return (0)
    i += (1 if i % 2 == 0 else 2)
  return (1)
  
i = 2
sum = 0

while (sum < 10001):
  if (is_prime(i) == 1):
    print(sum, i)
    sum += 1
  i += 1
  
print (i - 1)
