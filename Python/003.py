number = 600851475143
largestp = 0

for i in range(2,100000):
	if number % i == 0:
		number /= i
		largestp = i
		
print number, largestp