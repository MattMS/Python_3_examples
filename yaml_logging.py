"""
Print logging messages in Yaml format.

- https://docs.python.org/3/library/logging.html#formatter-objects

- https://docs.python.org/3/library/logging.html#logrecord-attributes
"""

import logging


logger = logging.getLogger(__name__)


def main():
	logger.debug('Business as usual.')
	logger.info('FYI')
	logger.warning('Barely a scratch.')
	logger.error('Just a flesh wound.')
	logger.critical('Hope you kept a backup.')


fmt = '''
- file: %(pathname)s
  function: %(funcName)s
  level: %(levelname)s
  line: %(lineno)s
  logger: %(name)s
  message: %(message)s
  time: %(asctime)s
'''.strip()


if __name__ == '__main__':
	logging.basicConfig(format=fmt, level=logging.DEBUG)

	main()
