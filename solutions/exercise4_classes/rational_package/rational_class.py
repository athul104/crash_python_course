import math
import sys
from continued_fractions import continued_fractions

class Rational():
	"""Documentation of class Rational"""
	
	def __init__(self, number, precision = 1e-10):
		"""
        	Initialize a Rational object.

		Parameters
		----------
		number : float or int
			 Number to convert to rational.
		precision : float (optional)
			    Precision (0 ≤ precision ≤ 1, default : 1e-10).
        """
		if not (0 <= precision <= 1):
			print("Error: precision must be between 0 and 1.")
			sys.exit(1)
			
		self.precision = precision
		self._numerator, self._denominator = self._approximate(number)
		
	def _approximate(self, number):
		"""Approximate number as (numerator, denominator) using continued fractions."""
		x = number # number
		return continued_fractions(x, self.precision)
		
	@property
	def numerator(self):
		"""Returns the numerator (read-only)."""
		return self._numerator
		
	@property
	def denominator(self):
		"""Returns the denominator (read-only)."""
		return self._denominator
		
	def __hash__(self):
		"""Make Rational hashable."""
		return hash((self.numerator, self.denominator))
		
			
	def __abs__(self):
		"""returns the absolute value of the rational number"""
		return Rational(abs(self.numerator/self.denominator), self.precision)
		
	def __str__(self):
		"""Returns the rational number as a string"""
		return f"{self.numerator}/{self.denominator}"
		
	def __repr__(self):
		"""Returns a string containing details about the decimal number and precision."""
		value = self.numerator/self.denominator
		return f"rational({value}, precision={self.precision})"
		
		
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
		
	def __truediv__(self, other): #division
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
		
	def __ge__(self, other): #greater than or equal to
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator >= self.denominator * other.numerator
		
	def __le__(self, other): #less than or equal to
		if not isinstance(other, Rational):
			other = Rational(other)
		return self.numerator * other.denominator <= self.denominator * other.numerator
		
	
	def __int__(self): #integer format
		return int(self.numerator/self.denominator)
		
	def __float__(self): #decimal format
		return self.numerator/self.denominator
		
if __name__ == "__main__":
	try:
		val = 0.5647
		rational = Rational(val)
		print(f"The rational form of {val} = {rational}")
		
	except ValueError as e:
		print(f"Error: {e}")

	except Exception as e:
		print(f"Unexpected Error: {e}")
			
			
			
		
		
