def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

def is_prime(n):
	if n == 1 or n == -1 or n == 0:
		return False
	else:
		prime = True
		i = 2
		while i <= n ** 0.5:
			if n % i == 0:
				prime = False
				break
			else:
				i += 1
		return prime

def degree_of_five(n):
	res = True
	while n > 1:
		if n % 5 != 0:
			res = False
			break
		else:
			n //= 5
	return res

def degree_of_two(n):
	res = True
	while n > 1:
		if n % 2 != 0:
			res = False
			break
		else:
			n //= 2
	return res