#!/usr/bin/env python3
from pathlib import Path
import os
import tomllib


PROJECT_ROOT = Path(__file__).parents[1]


def toml_version() -> str:
    with open(PROJECT_ROOT / "./pyproject.toml", "rb") as f:
        data = tomllib.load(f)

    res = data["tool"]["poetry"]["version"]
    assert isinstance(res, str)

    return res


if __name__ == "__main__":
    tag_version = os.getenv("GITHUB_REF")

    if tag_version is None:
        raise Exception("You have to export GITHUB_REF environment variable.")
    tag_version = tag_version.replace("refs/tags/", "")

    assert toml_version() == tag_version
