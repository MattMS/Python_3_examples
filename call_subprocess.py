"""
Demo of calling subprocesses.


Links
-----

- https://docs.python.org/3/library/io.html

- https://docs.python.org/3/library/subprocess.html
"""

from subprocess import call


def call_and_check_errors():
	call_args = ('wc', '-l', 'my_file')

	call_args_str = ' '.join(call_args)
	print(call_args_str)

	result = call(call_args)

	if 0 != result:
		print('Error during call.')


if '__main__' == __name__:
	call_and_check_errors()
