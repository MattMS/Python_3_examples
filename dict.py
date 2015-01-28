"""
Dictionary examples.

The intention is that you would use the code in the functions rather
than the functions themselves.
"""


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
