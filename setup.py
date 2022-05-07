from setuptools import setup
from anonymizer import __version__

setup(
	name='error-anonymizer',
	version=__version__,

	url='https://github.com/maskedband1t/error-anonymizer',
	author='Anurag Akkiraju',
	author_email='anurag.akkiraju@gmail.com',

	py_modules=['anonymizer'],
)