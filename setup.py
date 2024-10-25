from setuptools import setup, find_packages

setup(
    name='turtle-cli',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': [
            'turtle-cli = turtle_cli.cli:cli',
        ],
    },
)
