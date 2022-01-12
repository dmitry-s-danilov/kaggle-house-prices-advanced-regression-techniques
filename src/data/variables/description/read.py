from os import PathLike
from typing import Union

from .paths import file_path as path__
from .params import read_params as params__


def read(
    path:  Union[str, bytes, PathLike[str], PathLike[bytes], int] = path__,
    params: dict = params__,
):
    with open(path, **params) as file:
        content = file.read()
    return content
