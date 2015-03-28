from distutils.command.install import install
from distutils.core import setup
from distutils import log
import os
import json
import sys

kernel_json = {
    "argv": [sys.executable, 
	     "-m", "calysto_prolog", 
	     "-f", "{connection_file}"],
    "display_name": "Calysto Prolog",
    "language": "prolog",
    "name": "calysto_prolog"
}

class install_with_kernelspec(install):
    def run(self):
        install.run(self)
        from IPython.kernel.kernelspec import install_kernel_spec
        from IPython.utils.tempdir import TemporaryDirectory
        from metakernel.utils.kernel import install_kernel_resources
        with TemporaryDirectory() as td:
            os.chmod(td, 0o755) # Starts off as 700, not user readable
            with open(os.path.join(td, 'kernel.json'), 'w') as f:
                json.dump(kernel_json, f, sort_keys=True)
            install_kernel_resources(td, resource="calysto_prolog")
            log.info('Installing kernel spec')
            try:
                install_kernel_spec(td, 'calysto_prolog', replace=True)
            except:
                install_kernel_spec(td, 'calysto_prolog', user=self.user, replace=True)


svem_flag = '--single-version-externally-managed'
if svem_flag in sys.argv:
    # Die, setuptools, die.
    sys.argv.remove(svem_flag)

with open('calysto_prolog/__init__.py', 'rb') as fid:
    for line in fid:
        line = line.decode('utf-8')
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
      packages=['calysto_prolog'],
      install_requires=["metakernel"],
      cmdclass={'install': install_with_kernelspec},
      classifiers = [
          'Framework :: IPython',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 2',
      ]
)
