"""
Sorting things.
"""

my_dict = dict(B=2, a=1, c=3)
result = sorted(my_dict.keys(), key=str.lower)
expected = ['a', 'B', 'c']
assert result == expected
