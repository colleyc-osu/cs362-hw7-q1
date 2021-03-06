def fizzbuzz(r):
	result = ''
	for x in range(1, r+1):
		result += str(x)
		if x != r:
			result += '\t'
	return result
		