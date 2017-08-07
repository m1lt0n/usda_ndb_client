from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='usda_ndb_client',
    version='0.1.0',
    description=('A client for the USDA NDB API with information '
                 'about the nutrients of food'),
    long_description=long_description,
    url='https://github.com/m1lt0n/usd_ndb_client',
    keywords='usda ndb api nutrients food',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 4 - Beta'
    ],
    zip_safe=False,
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    tests_require=['pytest', 'mock', 'pytest-pep8'],
    author='Pantelis Vratsalis',
    author_email='pvratsalis@gmail.com'
)
