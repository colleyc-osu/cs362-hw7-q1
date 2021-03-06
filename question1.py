def fizzbuzz(r):
	result = ''
	for x in range(1, r+1):
		if (x % 15 == 0):
			result += "FizzBuzz"
		elif (x % 3 == 0):
			result += "Fizz"
		elif (x % 5 == 0):
			result += "Buzz"
		else:
			result += str(x)

		if x != r:
			result += '\t'

	return result
		