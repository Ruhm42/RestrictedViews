# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import os
from setuptools import find_packages, setup


def long_desc(root_path):
    FILES = ['README.rst']
    for filename in FILES:
        filepath = os.path.realpath(os.path.join(root_path, filename))
        if os.path.isfile(filepath):
            with open(filepath, mode='r') as f:
                yield f.read()

HERE = os.path.abspath(os.path.dirname(__file__))
long_description = "\n\n".join(long_desc(HERE))


def get_version(root_path):
    with open(os.path.join(root_path, 'django_restricted_views', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip('"\'')

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='django-restricted-views',
        version=get_version(HERE),
        packages=find_packages(),
        include_package_data=True,
        license='BSD License',
        description='Class based generic views that automatically check permissions',
        long_description=long_description,
        url='https://github.com/Ruhm42/django-restricted-views',
        download_url='https://github.com/Ruhm42/django-restricted-views/tarball/' + get_version(HERE),
        author='Romain Da Costa Vieira',
        author_email='romain.dacostavieira@gmail.com',
        install_requires=['Django>=1.8'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
        test_suite='django_timestampable.tests',
        zip_safe=False,
)
