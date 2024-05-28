from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import os

def read_requirements():
    """Read the requirements.txt file and return a list of requirements."""
    with open('requirements.txt') as req_file:
        return req_file.read().splitlines()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Run `npm install` in the node directory
        node_dir = os.path.join(self.install_lib, 'pybruno', 'node')
        subprocess.check_call(['npm', 'install'], cwd=node_dir)

setup(
    name='pybruno',
    version='0.1',
    packages=find_packages(),
    install_requires=read_requirements(),
    cmdclass={
        'install': PostInstallCommand,
    },
    include_package_data=True,
    package_data={
        'pybruno': ['node/*.js', 'node/package.json'],
    },
)
