from setuptools import setup

packages = [
    "appdirs",
    "asteval",
    "bw2analyzer>=0.9.4",
    "bw2calc>=1.7.1",
    "bw2data>=3.4.1",
    "bw2io>=0.6",
    "bw2parameters>=0.6.5",
    "docopt",
    "eight",
    "flask",
    "future",
    "lxml",
    "numpy",
    "peewee>=3.0",
    "psutil",
    "pyprind",
    "requests",
    "scipy",
    "stats_arrays>=0.4.2",
    "unicodecsv",
    "voluptuous",
    "whoosh",
    "xlrd",
    "xlsxwriter",
]

setup(
    name='brightway2',
    version="2.3",
    packages=["brightway2"],
    author="Chris Mutel",
    author_email="cmutel@gmail.com",
    license=open('LICENSE.txt').read(),
    install_requires=packages,
    url="https://bitbucket.org/cmutel/brightway2",
    long_description=open('README.rst').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
    ],
)
