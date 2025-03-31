def div(n, div_list = [2, 3, 5, 7]):
	"""A function to check if the integer 'n' is divisible by the numbers in the list 'div_list'.
	
	Args
	----
	n : int
	    The number to check for divisibilty.
	    
	div_list : list, optional
	    The list of numbers to check divisibility against (default: [2, 3, 5, 7]).
		
	Returns
	-------
	list :
	    A list of the divisors which divide the number 'n'.
		
	Raises
	------
	ValueError :
	    If 'n' is not an integer
		
	"""
	
	if type(n) != int: # To ensure 'n' is an integer
		raise ValueError('Input must be an integer.')
		
	return [d for d in div_list if n % d == 0] # list of divisors which divide the number 'n'
	
			

def mutual_div(a, b):
	""" A function to check if 'a' is divisible by 'b' and vice versa.
	
	Args
	----
	a : int or float
	    The first number.
	    
	b : int or float
	    The second number.
	    
	Returns
	-------
	tuple of bool:
	    (is 'a' is divisible by 'b', is 'b' is divisible by 'a').
	 
	Raises
	------
	ValueError:
	    If 'a' or 'b' is not a number (integer or float).
	ZeroDivisionError:
	    If 'a' or 'b' is zero.
	    
	"""
	if not isinstance(a, (int, float)) or not isinstance(b, (int, float)): # To check if both inputs are numbers
		raise ValueError("Both inputs must be numbers (integer or float).")
		
	if a == 0 or b == 0: # To ensure both inputs are non-zero number
		raise ZeroDivisionError("The input number can not be zero.")
	
	return (a % b == 0, b % a == 0)
	

def fibonacci(n):
	"""A function that calculates the Fibonacci sequence up to the n-th term

	Parameters
	----------
	n : int 
	the n-th term of the sequence

	Returns
	-------
	: list
	a list with the Fibonacci sequence
	
	
	"""
	
	ret_list = [] # list for Fibonacci sequence
	
	a, b = 0, 1 # first and second element
	
	for _ in range(n):
		ret_list.append(a) # adding elements to the sequence
		a, b = b, a + b # defining the next two consecutive elements
	return ret_list
	

def prime_eratosthenes(n):
	"""Function to compute prime numbers upto or below the integer 'n' using Eratosthenes algorithm.
	
	Args
	----
	n : int
	    The integer number upto or below which the prime numbers needs to be computed.
	    
	Returns
	-------
	list :
	    A list of prime numbers less than or equal to 'n'.
	    
	Raises
	------
	ValueError:
	    if 'n' is not an integer or greater than 1
	
	"""
	if type(n) != int or n < 2: # to ensure 'n' is an integer greater than 1
		raise ValueError("The input number must be an integer strictly greater than 1.")
		
	tmp_list = range(2, n+1) # list of numbers from 2 to n
	prime_list = [] # list for prime numbers
	
	while len(tmp_list) > 0:
		p = tmp_list[0] # first element of the list
		prime_list.append(p) # adds p to the prime_list
		tmp_list = [ x for x in tmp_list if x % p != 0 ] # removes all the multiples of p from tmp_list
		
	return prime_list
	


