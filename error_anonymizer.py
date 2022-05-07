#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# formatted using python black
import click
from pathlib import Path
__version__ = '1.2.4'

@click.command()
@click.argument(
    'error_file'
)
# unlimited substring arguments allowed
@click.argument("substrings" , nargs = -1)

def main(error_file, substrings):
	p = Path(error_file)
	txt = p.read_text()
	for substring in substrings:
		txt = txt.replace(substring, 'redacted')
	p.write_text(txt)

def hello_world():
    print("This is my first pip package!")

if __name__ == '__main__':
    main()