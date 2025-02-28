from setuptools import setup, find_packages


setup(
    name='TCGPokeParser',
    version='0.1',
    packages=find_packages(),
    description='TCGPokeParser',
    long_description=open('README.md').read(),
    install_requires=[i for i in open('requirements.txt').readlines()],
)