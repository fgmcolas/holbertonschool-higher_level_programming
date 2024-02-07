>>> print_square = __import__('4-print_square').print_square
>>> print_square(1)
#

>>> print_square(10)
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########

>>> print_square("chaussure")
Traceback (most recent call last):
TypeError: size must be an integer

>>> print_square(-5)
Traceback (most recent call last):
ValueError: size must be >= 0
