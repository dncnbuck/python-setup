from setuptools import setup, find_packages
import re

with open('version', 'r') as properties_file:
    properties = properties_file.read()
version = re.search(r'version=([0-9.\-A-Za-z]+)', properties).group(1)

setup(
    name='foo',
    version=version,
    description="Python project",
    classifiers=[],
    keywords='',
    author='Duncan Buck',
    author_email='dncnbuck@gmail.com',
    url='https://github.com/dncnbuck/python-setup',
    license='',
    packages=find_packages(exclude=['ez_setup', 'test']),
    package_data={
      'lib': []
    },
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # specify your requirements here:
        'jupyter',
        'requests'
    ],
    extras_require={
        'dev': [
            'flake8',
            'coverage',
            'pytest',
            'pytest-cov',
        ]
    },
    entry_points={
        'console_scripts': [
            'basic-lib = lib.__main__:main',
            ]
        },
)
