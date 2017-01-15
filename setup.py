from distutils.core import setup

setup(
    name='responseextract',
    version='2.0',
    packages=['responseextract'],
    url='https://github.com/handflucht/response-extract',
    license='Beerware',
    author='handflucht',
    author_email='',
    description='Executes an regular expression on a given url and returns the result.',
    requires=['requests'],
)
