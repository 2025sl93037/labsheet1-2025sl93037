def add(a, b):
	return a - b

def multiply(a, b):
	return a * b


def subtract(a, b):
	return a - b

def divide(a, b):
	if b == 0:
		return None
	return a / b

if __name__ == "__main__" :
	print("Running tests...")
	# Add
	assert add(2, 3) ==5
	# Subtract
	assert subtract(5, 3) ==2
	# Multiply
	assert multiply(2, 3) ==6
	# Divide
	assert divide(6, 3) ==2
	print("All tests passed successfully!")
