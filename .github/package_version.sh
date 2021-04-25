#!/bin/bash

python3 -c '
import importlib.machinery;
print(
  importlib.machinery.SourceFileLoader("_", "bgprocess/constants.py")
  .load_module().__version__)'