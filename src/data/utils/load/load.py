from typing import Callable, Union
from pathlib import Path
from pandas import DataFrame, read_csv

from .params import read_csv_params as params__
from .info import info as info__


def load(
    paths: Union[Path, list, dict],
    params: dict = params__,
    info: Union[bool, Callable] = False,
) -> Union[DataFrame, list, dict]:
    info_ = info if not info or isinstance(info, Callable) else info__

    if isinstance(paths, Path):
        data = read_csv(paths, **params)
        if info_:
            print(paths.name, end=':\n')
            info_(data)
    elif (
        isinstance(paths, list) and
        all(
            [
                isinstance(path, Path)
                for path in paths
            ]
        )
    ):
        data = [
            read_csv(path, **params)
            for path in paths
        ]
        if info_:
            for path, dataset in zip(paths, data):
                print(path.name, end=':\n')
                info_(dataset)
    elif (
        isinstance(paths, dict) and
        all(
            [
                isinstance(path, Path)
                for path in paths.values()
            ]
        )
    ):
        data = {
            key: read_csv(path, **params)
            for key, path in paths.items()
        }
        if info_:
            for key, dataset in data.items():
                print(key, paths[key].name, sep=': ')
                info_(dataset)
    else:
        data = None

    return data
