from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import setup, find_packages

constants = SourceFileLoader('constants', 'bgprocess/constants.py').load_module()

readme = (Path(__file__).parent / 'README.md').read_text()

setup(
    name="bgprocess",
    version=constants.__version__,

    author="Artёm IG",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/bgprocess_py#bgprocess',

    packages=find_packages(),
    install_requires=['func-timeout'],

    description="Reads the output of a process line-by-line with a time limit",

    long_description=readme,
    long_description_content_type='text/markdown',

    license='MIT',

    keywords="""process output timeout""".split(),

    # https://pypi.org/classifiers/
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development :: Documentation',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX",
    ],
)
