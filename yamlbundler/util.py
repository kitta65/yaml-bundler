from dataclasses import dataclass
from typing import Any, Generic, TypeVar

T = TypeVar("T")


@dataclass
class Result(Generic[T]):
    ok: bool
    value: T


def is_list_of_dict(list_: list[Any]) -> Result[list[dict[object, object]]]:
    ok = all([isinstance(x, dict) for x in list_])
    return Result(ok, list_ if ok else [])
