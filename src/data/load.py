from typing import Callable, Union
from pandas import DataFrame, read_csv

from .paths import file_paths as default_file_paths
from .params import load_params


def default_print_info(data_set: DataFrame):
    data_set.info(verbose=True)


def load(
    data_keys: Union[list[str], str] = None,
    print_info: Union[Callable[[DataFrame], None], bool] = False,
) -> Union[dict[str, DataFrame], DataFrame]:
    if isinstance(data_keys, str):
        return load(
            data_keys=[data_keys],
            print_info=print_info,
        ).get(data_keys)
    else:
        modified_file_paths = {
            data_key: default_file_paths[data_key]
            for data_key in data_keys
            if data_key in default_file_paths.keys()
        } if data_keys is not None else default_file_paths

        data_sets = {
            data_key: read_csv(file_path, **load_params)
            for data_key, file_path in modified_file_paths.items()
        }

        if print_info:
            modified_print_info = default_print_info \
                if not isinstance(print_info, Callable)\
                else print_info
            for data_key, data_set in data_sets.items():
                print(f'{data_key}: {modified_file_paths[data_key].name}')
                modified_print_info(data_set)

        return data_sets


if __name__ == '__main__':
    load(print_info=True)
