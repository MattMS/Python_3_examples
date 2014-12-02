"""
Python argparse example for a web server manager.
"""

import argparse


def init_app(config):
	return app


def runserver(args):
	pass


def syncdb(args):
	pass


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Manage application')
	# Includes '-h' option to show help messages

	parser.add_argument('-c', '--config',
		dest='config',
		default='settings',
		type=str,
		help='Config file to load settings from'
	)

	# Start creating sub-commands
	subparsers = parser.add_subparsers()


	# runserver starts a DEVELOPMENT server (do NOT use in production)
	runserver_parser = subparsers.add_parser('runserver', help='Launch server')
	runserver_parser.set_defaults(func=runserver)

	runserver_parser.add_argument('-H', '--host',
		dest='host',
		default='localhost',
		type=str,
		help='Host to start the server on'
	)

	runserver_parser.add_argument('-p', '--port',
		dest='port',
		default=80,
		type=int,
		help='Port number to start the server on'
	)


	# syncdb creates the models in the database
	syncdb_parser = subparsers.add_parser('syncdb', help='Create database from models')
	syncdb_parser.set_defaults(func=syncdb)


	# Parse arguments and perform the specified command
	args = parser.parse_args()
	args.func(args)
