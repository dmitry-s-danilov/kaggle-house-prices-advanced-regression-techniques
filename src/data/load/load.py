from typing import Callable, Any, Union
from pandas import DataFrame, read_csv

from .paths import file_paths as default_file_paths
from .params import load_params
from .print_info import print_info as default_print_info


def load(
    data_keys: Union[list, Any] = None,
    print_info: Union[Callable, bool] = False,
) -> Union[dict[str, DataFrame], DataFrame]:
    if (
        isinstance(data_keys, list) or
        data_keys is None
    ):
        file_paths = {
            data_key: default_file_paths[data_key]
            for data_key in data_keys
            if data_key in default_file_paths.keys()
        } if data_keys is not None else default_file_paths

        data_sets = {
            data_key: read_csv(file_path, **load_params)
            for data_key, file_path in file_paths.items()
        }

        if print_info:
            modified_print_info = print_info if isinstance(print_info, Callable) else default_print_info
            for data_key, data_set in data_sets.items():
                print(f'{data_key}: {file_paths[data_key].name}')
                modified_print_info(data_set)
    else:
        data_sets = load(
            data_keys=[data_keys],
            print_info=print_info,
        ).get(data_keys)

    return data_sets
