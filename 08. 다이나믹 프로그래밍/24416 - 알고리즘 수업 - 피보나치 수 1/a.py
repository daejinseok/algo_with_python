a = b = 1
for _ in range(5):
	a, b=b, a+b
	print(a, b)