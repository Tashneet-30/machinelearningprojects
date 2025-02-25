#responsible for creating ml application as package so that anybody can do the installation and deploy it

from setuptools import setup, find_packages

setup(
    name='mlproject',
    version='0.1.0',  # Add a valid version number
    author='Tashneet',
    author_email='tashneetkaur343@gmail.com',
    packages=find_packages(),  # Correct the typo in 'packages'
    install_requires=['pandas', 'numpy', 'seaborn']
)