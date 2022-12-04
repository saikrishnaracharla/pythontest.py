

def maximum(a, b, c):

	if (a >= b) and (a >= c):
		large = a

	elif (b >= a) and (b >= c):
		large = b
	else:
		large = c
		
	return large
a = 1
b = 14
c = 2
print(maximum(a, b, c))
