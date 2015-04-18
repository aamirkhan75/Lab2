try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'name': 'Lab2',
  'version': '0.0',
  'install_requires': ['nose']
}

setup(**config)
