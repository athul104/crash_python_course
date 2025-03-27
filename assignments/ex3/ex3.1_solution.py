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
	
	
if __name__ == '__main__':
	try:
		# ex_3.1.1
		print("")
		num = int(input("Enter an integer to check divisibility by 2, 3, 5, 7: ")) # input to check divisibilty by 2, 3, 5, 7
			
		div_result = div(num) # list of divisors of num
			
		#print
		if len(div_result) != 0:
			print(f'{num} is divisible by : {div_result}')
		else:
			print(f'{num} is not divisible by 2, 3, 5, or 7')
			
		print("")
			
	except ValueError as ve:
		print(f"Value Error: {ve}")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")
			
			
	try:
		#ex_3.1.2
		print("")
		num1 = float(input("Enter the first number to check mutual divisibility: ")) # input for the first number
		num2 = float(input("Enter the second number to check mutual divisibility: ")) # input for the second number

		mut_div_res = mutual_div(num1, num2) # tuple of bool

		a_by_b = mut_div_res[0] # is 'a' divisible by 'b'
		b_by_a = mut_div_res[1] # is 'b' divisible by 'a'
			
		#print
		if a_by_b:
			print(f'{num1} is divisible by {num2}.')
		else:
			print(f'{num1} is not divisible by {num2}.')

		if b_by_a:
			print(f'{num2} is divisible by {num1}.')
		else:
			print(f'{num2} is not divisible by {num1}.')	
			
		print("")	
		
			
			
	except ValueError as ve:
		print(f"Value Error: {ve}")

	except ZeroDivisionError as zde:
		print(f"Zero Division Error: {zde}")

	except Exception as e:
		print(f"An unexpected error occurred: {e}")
			
		
		
		
		

	
	
	
	    
		
	
		
	
	
		
