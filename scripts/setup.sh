#!/bin/bash
set -euo pipefail
cd $(dirname $0)

if ! command -v poetry; then
  # https://python-poetry.org/docs/#installation
  curl -sSL https://install.python-poetry.org | python3 -
fi

poetry install
