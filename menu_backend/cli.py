# -*- coding: utf-8 -*-

import click
import logging
from menu_backend.commands.InstallDb import manageDb
from menu_backend.commands.WebService import startWebService

@click.group()
def cli():
    pass

def main():
	FORMAT = '%(asctime)-15s - %(levelname)s - %(message)s'
	logging.basicConfig(format=FORMAT, level=logging.DEBUG)
	cli.add_command(manageDb)
	cli.add_command(startWebService)

if __name__ == '__main__':
	sys.exit(main())  # pragma: no cover
	cli()