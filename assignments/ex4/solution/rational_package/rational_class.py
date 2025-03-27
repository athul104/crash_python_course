import math
from continued_fractions import continued_fractions

class Rational():
	"""Documentation of class Rational"""
	
	def __init__(self, number, precision = 1e-5):
		"""
        	Initialize a Rational object.

		Parameters
		----------
		number : float or int
			 Number to convert to rational.
		precision : float (optional)
			    Precision (0 ≤ precision ≤ 1, default : 1e-5).
        """
		if not (0 <= precision <= 1):
			print("Error: precision must be between 0 and 1.")
			sys.exit(1)
			
		self.precision = precision
		self.numerator, self.denominator = self._approximate(number)
		
	def _approximate(self, number):
		"""Approximate number as (numerator, denominator) using continued fractions."""
		
		x = number # number
		return continued_fractions(x, self.precision)
			
	def __abs__(self):
		return Rational(abs(self.numerator / self.denominator), self.precision)
		
	def __str__(self):
		return f"{self.numerator}/{self.denominator}"
	def __repr__(self):
		return f"rational({self.numerator / self.denominator}, precision={self.precision})"
		
	# Arithmatic operators
	def __add__(self, other): #addition
		if not isinstance(other, Rational):
			other = Rational(other)
		num = self.numerator * other.denominator + other.numerator * self.denominator
		deno = self.denominator * other.denominator
		return Rational(num/deno, self.precision)
		
	def __sub__(self, other): #substraction
		if not isinstance(other, Rational):
			other = Rational(other)
		num = self.numerator * other.denominator - other.numerator * self.denominator
		deno = self.denominator * other.denominator
		return Rational(num/deno, self.precision)
		
	def __mul__(self, other): #multiplication
		if not isinstance(other, Rational):
			other = Rational(other)
		num = self.numerator * other.numerator
		deno = self.denominator * other.denominator
		return Rational(num/deno, self.precision)
		
	def __div__(self, other): #division
		if not isinstance(other, Rational):
			other = Rational(other)
		if other.numerator == 0:
			raise ZeroDivisionError("Cannot divide by zero.")
		num = self.numerator * other.denominator 
		deno = self.denominator * other.numerator
		return Rational(num/deno, self.precision)
		
	# Comparison operators
	def __eq__(self, other): #equal to
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator == self.denominator * other.numerator
		
	def __gt__(self, other): #greater than
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator > self.denominator * other.numerator
		
	def __lt__(self, other): #less than
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator < self.denominator * other.numerator
		
	def __geq__(self, other): #greater than or equal to
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator >= self.denominator * other.numerator
		
	def __leq__(self, other): #less than or equal to
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator <= self.denominator * other.numerator
		
	
	def __int__(self): #integer format
		return int(self.numerator/self.denominator)
		
	def __float__(self): #decimal format
		return self.numerator/self.denominator
			
			
			
		
		
