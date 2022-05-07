from setuptools import setup, find_packages
from error_anonymizer import __version__
with open("README.md") as f:
    readme = f.read()
setup(
	name='error_anonymizer',
	version=__version__,
	#description=readme,

	url='https://github.com/maskedband1t/error-anonymizer',
	author='Anurag Akkiraju',
	author_email='anurag.akkiraju@gmail.com',

	py_modules=['error_anonymizer'],
	packages=find_packages(),

	install_requires=[
		'setuptools',
		'click==8.1.3',
		'pathlib',
	],

	entry_points={
		'console_scripts': [
			'main=error_anonymizer:main',
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