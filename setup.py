from setuptools import setup

setup(
    name='uptake',
    version='0.0.1',
    packages=['page', 'test'],
    install_requires=['selenium==2.53.1'],
    test_suite='test',
    url='',
    license='BSD',
    author='Aaron Brenzel',
    author_email='aaronbrenzel@gmail.com',
    description='Code sample for the Uptake homepage'
)
