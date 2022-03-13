from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Common algorithms implemented in python'

setup(
    name="algorithms",
    version=VERSION,
    description=DESCRIPTION,
    long_description='',
    author='Ashwin',
    packages=find_packages(),
    install_requires = ['hashlib', 'pycrypto'],
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)