x = 1
y = 2
sum = y

while x < 4000000 and y < 4000000:
	if x < y:
		x += y
		if x % 2 == 0:
			sum += x
	elif y < x:
		y += x
		if y % 2 == 0:
			sum += y
			
print sum