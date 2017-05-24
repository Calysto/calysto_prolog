import sys
import io

from setuptools import find_packages, setup

with io.open('calysto_prolog/__init__.py', encoding="utf-8") as fid:
    for line in fid:
        if line.startswith('__version__'):
            __version__ = line.strip().split()[-1][1:-1]
            break

with open('README.md') as f:
    readme = f.read()

setup(name='calysto_prolog',
      version=__version__,
      description='A Prolog kernel for Jupyter that can use Python libraries',
      long_description=readme,
      url="https://github.com/Calysto/calysto_prolog",
      author='Douglas Blank',
      author_email='doug.blank@gmail.com',
      packages=find_packages(include=['calysto_prolog', 'calysto_prolog.*'],),
      package_data={'calysto_prolog': ["images/*.png"]},
      install_requires=["metakernel"],
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
      ]
)
