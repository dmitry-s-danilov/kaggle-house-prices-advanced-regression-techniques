from pandas import read_csv

from .paths import (
    data_home_path,
    data_files,
    data_file_paths,
)
from .params import data_load_params


def main():
    data_sets = {
        data_key: read_csv(data_file_path, **data_load_params)
        for data_key, data_file_path in data_file_paths.items()
    }

    print(f'datasets path: {data_home_path}')

    for data_key, data_set in data_sets.items():
        print(f'\n{data_key} dataset: {data_files[data_key]}\n')
        data_set.info()
