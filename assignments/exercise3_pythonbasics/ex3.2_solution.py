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
	
def _test1(lst):
	"""A test function to list the elements with even index in the list 'lst'.
	
	Args
	----
	lst : list
	      List from which the even index elements needs to be extracted.
	
	Returns
	-------
	List :
	      A lits with even index elements from input list.
	"""
	
	return [lst[i] for i in range(len(lst)) if i % 2 == 0]
	
	
def _test2(lst):
	"""A test function to list the elements with odd index in the list 'lst'.
	
	Args
	----
	lst : list
	      List from which the odd index elements needs to be extracted.
	
	Returns
	-------
	List :
	      A lits with odd index elements from input list.
	"""
	
	return [lst[i] for i in range(len(lst)) if i % 2 != 0]
	
	
if __name__ == '__main__':

	try:
		print("")
		num = int(input("Enter how many initial terms of the Fibonacci sequence you require: ")) #The number of terms in the Fibonacci sequence
		fibonacci_list = fibonacci(num) # fibonacci sequence
		print(f"The first {num} elements of the Fibonacci sequence: ")
		print(fibonacci_list)
		print("")
		
		print("The elements with even index in the Fibonacci sequence:")
		print(_test1(fibonacci_list))
		print("")
		print("The elements with odd index in the Fibonacci sequence:")
		print(_test2(fibonacci_list))
		print("")
		
	except ValueError as ve:
		print(f"A value error has occured: {ve}")
	
	except Exception as e:
        	print(f"An unexpected error occurred: {e}")
		
		
	
	
	
	
	
	
	
