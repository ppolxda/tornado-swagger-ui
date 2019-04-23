from codecs import open
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'tornado_swagger_ui/README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tornado_swagger_ui',
    version='0.1',
    description='Swagger UI for Tornado',
    long_description=long_description,
    zip_safe=False,

    url='https://github.com/DominguesM/tornado-swagger-ui',

    author='Maicon Domingues',
    author_email='dominguesm@outlook.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='tornado swagger',
    packages=['tornado_swagger_ui'],
    install_requires=['tornado'],
    package_data={
        'tornado_swagger_ui': [
            'LICENSE',
            'README.md',
            'assets/VERSION',
            'assets/LICENSE',
            'assets/README.md',
            'assets/*.html',
            'assets/*.js',
            'assets/*.css',
            'assets/*.png'
        ],
    }
)
