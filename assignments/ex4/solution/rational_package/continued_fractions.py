import math

def continued_fractions(x, precision):
	"""Approximate number as (numerator, denominator) using continued fractions."""
	
	a_0 = math.floor(x) #floor(number)
		x_i = x - a_0 #x_1 = x - a_0
		n_m, n_0 = 0, 1 # initial values n_{-1}, n_0
		d_m, d_0 = 1, 0 # initial values d_{-1}, d_0
		
		while True:
			# this iteration starts from i = 1
			n_i = a_0 * n_0 + n_m # n_i = a_{i-1} * n_{i-1} + n_{i-2}
			d_i = a_0 * d_0 + d_m # d_i = a_{i-1} * d_{i-1} + d_{i-2}
			
			
			if abs(n_i/d_i - x) < precision:
				return n_i, d_i #return if precision is reached
				
			n_m, n_0 = n_0, n_i #redefining the numerators
			d_m, d_0 = d_0, d_i #redefining the denominators
			
			a_0 = math.floor(1/x_i) if x_i != 0 else 0 #a_i = floor(1/x_i)
			x_i = (1/x_i) - a_0 if x_i != 0 else 0 #next x_{i+1}
