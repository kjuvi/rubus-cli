from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='rubus',
    version='1.0',
    description='CLI to interact with a Rubus API instance',
    long_description=readme,
    author='Quentin Vaucher',
    author_email='quentin.vaucher@protonmail.com',
    url='https://github.com/xiorcale/rubus-cli',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        rubus=rubus.rubus:cli
    '''
)
