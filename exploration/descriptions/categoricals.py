#!/bin/python

from pandas import option_context
from contest.exploration.descriptions.categoricals import describe

data_description = describe()

if __name__ == '__main__':
    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        # 'display.max_colwidth', None,
        'display.width', None,
    ):
        print(data_description)
