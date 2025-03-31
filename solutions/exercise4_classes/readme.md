# Class 'Rational'

In this directory you can find a python package, `rational_package` and a jupyter notebook, `Rational_test.ipynb` which contains the solutions for exercise 4, relevant to buliding a class object for handling **Rational Numbers**.

## rational_package

This python package contains two python scripts `rational_class.py` and `continued_fractions.py`. In `rational_class.py`, we define the class object called **Rational**, which takes a number as a positional argument and an optional keyword argument 'precision'. This class converts any real number into a rational form, within the precision specified (which is by default '1e-10'). 

The number is approximated into rational form using the **Continued fractions** algorithm, which is defined in `continued_fractions.py`. This module has been imported in `rational_class.py`.

In this class, the numerator and denominator of the rational number is stored internally as properties, hence they cannot be modified directly. This ensures immutability. The sign of the real number is stored in the numerator of the approximated rational number. The fraction will be given in its reduced form where both numerator and denominator has no common factors other than 1.

The class **Rational** has the following operators or dunder functions:
- `__hash__`: Returns a unique integer (hash value) for a number. This gives the advantage of using numbers of rational type as keys in dictionaries and as elements in sets.
- `__abs__`: Returns the absolute value of the rational number.
- `__str__`: Returns rational number as a string.
- `__repr__`: Returns a "formal" string representation of the object ( for eg. `'rational( 0.5, precision=1.e-5)'`).
- Arithmatic operators: `__add__`, `__mul__`, `__truediv__`, `__sub__`.
- Comparison operators: `__eq__`, `__gt__`, `__ge__`, `__lt__`, `__le__`.
- `__int__`: Returns the rational number as integer.
- `__float__`: Returns the rational number as float.


The external libraries used in these two scripts are `math` and `sys`.

## Rational_test.ipynb

This jupyter notebook contains some tests that are designed to check if the class **Rational**, that we defined in `rational_package` for handling rational numbers are working well. The description reagrading each test are given in the notebook along with the code.






