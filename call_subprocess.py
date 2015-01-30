"""
Demo of calling subprocesses.


Links
-----

- https://docs.python.org/3/library/io.html

- https://docs.python.org/3/library/subprocess.html
"""

from subprocess import CalledProcessError, call, check_output
import sys


def call_and_check_errors():
	call_args = ('touch', sys.argv[0])

	call_args_str = ' '.join(call_args)
	print(call_args_str)

	result = call(call_args)

	if 0 != result:
		print('Error during call.')


def call_and_get_output():
	call_args = ('wc', '-l', sys.argv[0])

	call_args_str = ' '.join(call_args)
	print(call_args_str)

	try:
		stdout = check_output(call_args)
		print(stdout)
	except CalledProcessError:
		print('Error during call.')


if '__main__' == __name__:
	call_and_get_output()
