from setuptools import setup, find_packages

setup(
    name='simple-subnet',
    version='0.1',
    packages=find_packages(),
    url='http://github.com/tinglebrody/Subnetting',
    license='MIT License',
    author='Brody Tingle',
    author_email='brodyleehumphrey@gmail.com',
    description='A lightweight subnetting tool',
    long_description=open('README.md').read(),
    install_requires=[
        'ipaddress'
        # Add any other dependencies here
    ],
    
)