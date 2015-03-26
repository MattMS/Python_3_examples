"""
Dictionary examples.

The intention is that you would use the code in the functions rather
than the functions themselves.
"""


def create_dict():
	"""
	Create a new dictionary.

	Example from: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

	>>> a = dict(one=1, two=2, three=3)
	>>> b = {'one': 1, 'two': 2, 'three': 3}
	>>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
	>>> d = dict([('two', 2), ('one', 1), ('three', 3)])
	>>> e = dict({'three': 3, 'one': 1, 'two': 2})
	>>> a == b == c == d == e
	True
	"""

	return dict()


def copy_dict(other_dict):
	"""
	Returns a copy of the dictionary, separate from the original.

	This separation is only at the top-level keys.

	If you delete a key in the original, it will not change the copy.

	>>> d1 = dict(a=1, b=2)
	>>> d2 = dict(**d1)
	>>> del d1['a']
	>>> 'a' in d1
	False
	>>> 'a' in d2
	True

	If any of the top-level values are mutable (list, dict) then changes
	to the original will appear in the copy.

	>>> d1 = dict(a=[1, 2], b=[3, 4])
	>>> d2 = dict(**d1)
	>>> d1['a'].pop()
	2
	>>> d1['a']
	[1]
	>>> d1['a'] == d2['a']
	True

	Tested in Python 3.4.
	"""

	new_dict = dict(**other_dict)
	return new_dict


def update_dict(original, other):
	"""
	Update the original dict with values from the other.

	If you delete a key in the other, it will not change the original.

	>>> d1 = dict(a=1)
	>>> d2 = dict(b=2)
	>>> d1
	{'a': 1}
	>>> d2
	{'b': 2}

	>>> d1.update(d2)
	>>> d1
	{'a': 1, 'b': 2}
	>>> d2
	{'b': 2}

	Tested in Python 3.4.
	"""

	original.update(other)
	return original
