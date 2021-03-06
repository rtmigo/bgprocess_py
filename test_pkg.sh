#!/bin/bash
set -e

# check we can extract the package version
.github/package_version.sh

source pyrel.sh

# build package, install it into virtual
# environment with pip
pyrel_test_begin

# check, that we can import this module by name
# (so it's installed)
python3 -c "import bgprocess"
echo "Imported!"

# remove generated package
pyrel_test_end