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
	
if __name__ == '__main__':

	print("")
	print(f"The list of prime numbers upto 100: ")
	print(f"{prime_eratosthenes(100)}") # list of prime numbers upto 100
	print("")
		

		
	
	
	
