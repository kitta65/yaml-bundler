from dataclasses import dataclass
from pathlib import Path
import argparse


@dataclass
class Args:
    filename: Path
    inplace: bool
    out: Path


def main(args: Args) -> str:
    print(args)
    return str(args)


def parse_args() -> Args:
    parser = argparse.ArgumentParser(
        prog="YAML Bundler", description="Handle !include tag and bundle YAML files."
    )
    parser.add_argument("filename", type=Path)
    parser.add_argument("-i", "--inplace", action="store_true")
    parser.add_argument("-o", "--out", type=Path)
    args = parser.parse_args()

    return Args(
        filename=args.filename,
        inplace=args.inplace,
        out=args.output,
    )


if __name__ == "__main__":
    args = parse_args()
    main(args)
