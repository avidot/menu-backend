# -*- coding: utf-8 -*-

import os
import click
import logging
from commands.InstallDb import installDb
from commands.WebService import startWebService

@click.group()
def cli():
    pass

if __name__ == '__main__':
	FORMAT = '%(asctime)-15s - %(levelname)s - %(message)s'
	logging.basicConfig(format=FORMAT, level=logging.DEBUG)
	cli.add_command(installDb)
	cli.add_command(startWebService)
	cli()