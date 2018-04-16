from setuptools import setup, find_packages


setup(name='pandleau',
      version='0.1dev',
      packages=find_packages(exclude=['tests*']),
      license='MIT',
      description='A quick and easy way to convert a Pandas DataFrame to a Tableau extract.',
      long_description=open('README.md').read(),
      install_requires=['pandas','numpy','tableausdk'],
      author='Benjamin Wiley',
      author_email='bewi7122@colorado.edu',
      url='https://github.com/bwiley1/pandleau',
      download_url='https://github.com/bwiley1/pandleau/archive/1.0.0.tar.gz',
      py_modules=['pandleau'],
      keywords='tableau pandas extract tde',
      classifiers=['Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'])
