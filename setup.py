from pathlib import Path

from setuptools import setup, find_packages

readme = (Path(__file__).parent / 'README.md').read_text()
#readme = "# "+readme.partition("\n#")[-1]

setup(
  name="bgprocess",
  version="1.0.0",

  author="Artёm IG",
  author_email="ortemeo@gmail.com",
  url='https://github.com/rtmigo/bgprocess_py',

  packages=find_packages(),
  install_requires=[],

  description="Reads the output of a process line-by-line with a time limit",

  long_description=readme,
  long_description_content_type='text/markdown',

  license='MIT',

  keywords="""process output timeout""".split(),

  # https://pypi.org/classifiers/
  classifiers=[
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    'License :: OSI Approved :: MIT License',
    'Topic :: Software Development :: Documentation',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Operating System :: POSIX",
  ],


  # test_suite='nose.collector',
  # tests_require=['nose'],
  # zip_safe=False
)