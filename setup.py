from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='wb-inventory',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      maintainer='ElevenCraft Inc.',
      maintainer_email='matt@11craft.com',
      url='https://github.com/wherebee/wb-inventory/',
      license='Apache 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'djangorestframework >= 0.2.0',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
