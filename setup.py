from setuptools import find_packages, setup
setup(
    name='encodedecodelib',
    packages=find_packages(include=['encodedecodelib']),
    version='0.1.0',
    description='Library to encode and decode string values',
    author='Me',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)