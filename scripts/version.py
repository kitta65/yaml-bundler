#!/usr/bin/env python3
from pathlib import Path
import os
import tomllib


PROJECT_ROOT = Path(__file__).parents[1]


def toml_version() -> str:
    with open(PROJECT_ROOT / "./pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    return data["tool"]["poetry"]["version"]


if __name__ == "__main__":
    tag_version = os.getenv("GITHUB_REF")

    if tag_version is None:
        raise Exception("Do not run this script locally.")
    tag_version = tag_version.replace("refs/tags/", "")

    assert toml_version() == tag_version