from pathlib import Path

import pytest

from yamlbundler.command import parse_args, Args
from yamlbundler.exception import YAMLBundlerException


@pytest.mark.parametrize(
    "args,expected",
    [
        (
            ["filepath1", "--inplace"],
            Args(input=Path("filepath1"), output=Path("filepath1")),
        ),
        (["filepath1", "-i"], Args(input=Path("filepath1"), output=Path("filepath1"))),
        (
            ["filepath1", "--output", "filepath2"],
            Args(input=Path("filepath1"), output=Path("filepath2")),
        ),
        (
            ["filepath1", "-o", "filepath2"],
            Args(input=Path("filepath1"), output=Path("filepath2")),
        ),
    ],
)
def test_parse_args_valid(args: list[str], expected: Args) -> None:
    actual = parse_args(test_args=args)
    assert actual == expected


@pytest.mark.parametrize(
    "args",
    [
        ["filepath1", "-i", "-o", "filepath2"],
        ["filepath1"],
    ],
)
def test_parse_args_invalid(args: list[str]) -> None:
    with pytest.raises(YAMLBundlerException):
        parse_args(test_args=args)
