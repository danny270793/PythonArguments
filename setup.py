from setuptools import setup, find_packages
from codecs import open
from os import path

here=path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description=file.read()
setup(
    name='arguments',
    version='0.1.0',
    description='A command line arguments parser library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/danny270793/Arguments',
    author='Danny Vaca',
    license='MIT',
    packages=['arguments'],
    author_email='danny270793@gmail.com',
    zip_safe=False
)