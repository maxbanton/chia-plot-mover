#!/usr/bin/env bash

if ! python3 -c 'import sys; assert sys.version_info >= (3,7)' 2> /dev/null;
then
  echo 'Found an unsupported version of Python'
  echo 'Python 3.7+ required. Update before proceeding with the installation'
  exit 1
fi

# Create virtual environment
python3 -m venv .venv

source .venv/bin/activate

python -m pip install poetry
poetry install --no-dev

deactivate