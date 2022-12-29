from pathlib import Path

from yamlbundler.command import parse_args, Args


def test_parse_args() -> None:
    actual = parse_args(test_args=["filepath", "--inplace"])
    expected = Args(input=Path("filepath"), output=Path("filepath"))
    assert actual == expected
