from pathlib import Path
import os

import yaml
import pytest

from yamlbundler.command import main, parse_args, Args
from yamlbundler.exception import YAMLBundlerException


TESTCASE_PATH = Path("testcases")


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


def list_input_files(valid: bool) -> list[Path]:
    path = TESTCASE_PATH / ("valid" if valid else "invalid")
    input_strs = os.listdir(path)
    input_paths = filter(lambda x: os.path.isfile(path / x), input_strs)

    return [path / x for x in input_paths]


@pytest.mark.parametrize(
    "path",
    list_input_files(valid=True),
)
def test_main_valid(path: Path, tmp_path: Path) -> None:
    actual = main(Args(input=path, output=tmp_path / path.name))
    with open(path.parent / "expected" / path.name, "r") as f:
        expected = yaml.full_load(f)
    assert actual == expected
