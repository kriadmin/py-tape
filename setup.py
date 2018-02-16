from setuptools import setup

setup(name='py-tape',
      version='0.0.1',
      description='A testing framework based on tape',
      url='http://github.com/storborg/funniest',
      author='Rohit Tanwar',
      author_email='mst10041967@gmail.com',
      license='MIT',
      packages=['py-tape'],
      entry_points = {
        'console_scripts': ['py-tape=tape.main:main']
    }
      )