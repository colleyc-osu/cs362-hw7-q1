def fizzbuzz(r):
	result = ''
	for x in range(1, r+1):
		if (x % 3 == 0):
			result += "Fizz"
		else:
			result += str(x)

		if x != r:
			result += '\t'

	return result
		