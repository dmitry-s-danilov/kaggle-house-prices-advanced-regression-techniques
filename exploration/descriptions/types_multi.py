#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.descriptions import default_data_keys as data_keys
from contest.exploration.descriptions.types import (
    describe,
    default_multi_params as describe_params,
)

if __name__ == '__main__':
    data_sets = load(data_keys)
    data_description = describe(data_sets, **describe_params)

    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        'display.width', None,
    ):
        print(data_description)
