a = 1
b = 2
c = 997

while (1):
  if (a * a + b * b == c * c):
    print(a * b * c)
    break
  if (b * b + a * a >= c * c):
    a += 1
    b = a + 1
    c = 1000 - a - b
  b += 1
  c -= 1
