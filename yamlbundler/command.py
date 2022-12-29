from dataclasses import dataclass
from pathlib import Path
import argparse
import contextlib

import yaml

from yamlbundler.exception import YAMLBundlerException


@dataclass(eq=True)
class Args:
    input: Path
    output: Path


def main(args: Args) -> object:
    abspath = args.input.resolve()

    with (
        open(abspath, "r") as f,
        contextlib.chdir(abspath.parent),
    ):
        obj = yaml.full_load(f)

    with open(args.output, "w") as f:
        f.write(yaml.dump(obj))

    return obj


def parse_args(test_args: list[str] | None = None) -> Args:
    parser = argparse.ArgumentParser(
        prog="YAML Bundler", description="Handle !include tag and bundle YAML files."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("-i", "--inplace", action="store_true")
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args(test_args)

    if not args.inplace and args.ouput is None:
        raise YAMLBundlerException("specify --output or --inplace parameter")

    return Args(
        input=args.input,
        output=args.input if args.inplace else args.output,
    )


if __name__ == "__main__":
    args = parse_args()
    main(args)
