from typing import Callable, Union
from pathlib import Path
from pandas import DataFrame, read_csv

from .paths import file_paths as default_file_paths
from .params import load_params as default_load_params


def default_print_info(data_set: DataFrame):
    data_set.info(verbose=True)


def load(
    file_paths: dict[str, Path] = default_file_paths,
    load_params: dict = default_load_params,
    data_keys: list[str] = None,
    print_info: Union[Callable[[DataFrame], None], bool] = False,
) -> dict[str, DataFrame]:
    modified_data_keys = [
        data_key
        for data_key in data_keys
        if data_key in file_paths.keys()
    ] \
        if data_keys is not None \
        else file_paths.keys()

    data_sets = {
        data_key: read_csv(file_paths[data_key], **load_params)
        for data_key in modified_data_keys
    }

    if print_info:
        modified_print_info = default_print_info \
            if not isinstance(print_info, Callable)\
            else print_info
        for data_key, data_set in data_sets.items():
            print(f'{data_key}: {file_paths[data_key].name}')
            modified_print_info(data_set)

    return data_sets
