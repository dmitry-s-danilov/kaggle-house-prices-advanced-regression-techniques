#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.tools import describe
from contest.exploration.descriptions.uniques import single_describe_params as describe_params

data_key = 'train'

if __name__ == '__main__':
    description = describe(
        data=load(data_keys=data_key),
        **describe_params
    )

    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        'display.width', None,
    ):
        print(description)
