#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.descriptions.objects import (
    describe,
    single_transformers as describe_transformers,
)

data_key = 'train'

if __name__ == '__main__':
    data_set = load(data_keys=data_key)
    data_description = describe(
        data=data_set,
        transformers=describe_transformers,
    )

    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        'display.width', None,
    ):
        print(data_description)
