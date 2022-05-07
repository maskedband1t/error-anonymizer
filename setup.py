from setuptools import setup, find_packages
from error_anonymizer.anonymizer import __version__

setup(
	name='error_anonymizer',
	version=__version__,

	url='https://github.com/maskedband1t/error-anonymizer',
	author='Anurag Akkiraju',
	author_email='anurag.akkiraju@gmail.com',

	py_modules=['error-anonymizer'],
	packages=find_packages(),

	install_requires=[
		'setuptools',
		'click',
		'pathlib'
	],

	entry_points={
		'console_scripts': [
			'main=anonymizer:main',
		],
	},

	classifiers=[
		'Intended Audience :: Developers',

		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
    	],

	extra_test = [
    		'pytest>=4',
    		'pytest-cov>=2',
	],
)