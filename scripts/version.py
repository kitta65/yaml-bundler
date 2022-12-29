#!/usr/bin/env python3
from pathlib import Path
import tomllib


PROJECT_ROOT = Path(__file__).parents[1]

with open(PROJECT_ROOT / "./pyproject.toml", "rb") as f:
    data = tomllib.load(f)
    print(data["tool"]["poetry"]["version"], end="")
