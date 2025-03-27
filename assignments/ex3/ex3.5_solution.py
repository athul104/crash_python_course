from my_module import div, prime_eratosthenes

def factorisation(n):
	"""Function to decompse the positive integer 'n' in terms of its prime factors.
	
	Args
	----
	n : int
	    Number to be decomposed in to prime factors.
	   
	Returns
	-------
	dict:
	    The keys are the prime factors and the corresponding values will be the powers of the factors in the decomposition.
	    
	Raises
	------
	ValueError:
	    If 'n' is not a positive integer.
	    
	"""
	
	if type(n) != int and n > 0: # To ensure 'n' is an integer and positive
		raise ValueError('Input must be a positive integer.')
	
	if n == 1: # since n = 1 is not a prime number this has to be added separately
		return {1 : 1}
		
	else:
		prime_list = prime_eratosthenes(n) # list of prime numbers upto or below 'n'
		factors_list = div(n, prime_list) # list of prime factors of 'n' (unique occurances)
		
		factors_dict = {} # the dictionary to which the prime factors are added
		
		for factor in factors_list:
			count = 0
			while n % factor == 0:
				n = n // factor
				count += 1
			factors_dict[factor] = count # stores the exponent of each prime factor
		
		return factors_dict
	
if __name__ == '__main__':
	try:
		
		check_list = range(1, 101) # list from 1 to 100
		
		print("")
		print("Finding the prime factor decomposition of numbers from 1 to 100")
		print("")
		for n in check_list: # finding the prime factor decomposition of 1 to 100
			decomposed_dict = factorisation(n) # dictionary with prime factor decomposition of each n
			decomposition = ' x '.join([f'{key}^{value}' if value !=1 else f"{key}" for key, value in decomposed_dict.items()]) # a string which expresses the prime 				factors and its exponents in mathematical form (eg: for 20, it will be 2^2 x 5)
			print(f"{n} = {decomposition}") # printing the decomposition in mathematical form
			print("")
		
	except ValueError as ve:
		print(f"Value Error: {ve}")


	except Exception as e:
		print(f"An unexpected error occurred: {e}")
		
			
				
	

		
	
	
	
