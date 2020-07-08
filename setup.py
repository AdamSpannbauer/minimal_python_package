# This file is if we want to be able to pip install it & upload the package to pypi

from setuptools import setup


setup(name='my_pkg',
      version='0.0.1',
      description='Minimal example python package',
      author='Adam Spannbauer',
      author_email='spannbaueradam@gmail.com',
      url='https://github.com/AdamSpannbauer/minimal_python_package',
      packages=['my_pkg'],
      license='MIT',
      )
