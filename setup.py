from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Run `npm install` in the node directory
        node_dir = os.path.join(self.install_lib, 'my_hybrid_package', 'node')
        subprocess.check_call(['npm', 'install'], cwd=node_dir)

setup(
    name='pybruno',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # your python dependencies
    ],
    cmdclass={
        'install': PostInstallCommand,
    },
    include_package_data=True,
    package_data={
        'pybruno': ['node/*.js', 'node/package.json'],
    },
)