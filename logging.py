"""
Python logging example.

- https://docs.python.org/2/library/logging.html
- https://docs.python.org/2/howto/logging.html
"""

import logging


logger = logging.getLogger(__name__)


def main(a):
	logger.debug('Started main().')

	if a:
		logger.info('The argument "%s" is True!', a)
	else:
		logger.error('The argument "%s" is False!', a)


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)

	main(12)