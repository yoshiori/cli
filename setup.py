from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'launchable',
    version = '0.0.2',
    license = 'MIT',
    author = 'Satoshi Asano',
    url = 'https://launchableinc.com/',
    author_email = 'sasano@launchableinc.com',
    description = 'Launchable CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires = ['setuptools'],
    packages = ["launchable"],
    entry_points = {
        'console_scripts': [
            'launchable = launchable.cli:main',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)