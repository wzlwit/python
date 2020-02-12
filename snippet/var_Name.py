
""" 
With Python 3.8 one can simply use f-string debugging feature:

>>> foo = dict()
>>> f'{foo=}'.split('=')[0]
'foo' 

"""
# f-strings support = for self-documenting expressions and debugging
# https://docs.python.org/release/3.8.0/whatsnew/3.8.html

foo = dict()
f'{foo=}'.split('=')[0]
