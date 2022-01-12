from typing import Callable, Union
from pandas import DataFrame

from ..utils import load as load__
from .paths import file_paths as paths__


def load(
    keys,
    info: Union[bool, Callable] = False,
) -> Union[DataFrame, dict]:
    if isinstance(keys, list):
        paths = {
            key: paths__[key]
            for key in keys
            if key in paths__.keys()
        }
    else:
        paths = paths__.get(keys)

    return load__(
        paths=paths,
        info=info,
    )
