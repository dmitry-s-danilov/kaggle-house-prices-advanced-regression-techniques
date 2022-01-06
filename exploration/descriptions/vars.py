#!/bin/python

from pandas import option_context
from contest.data import vars_description as data_description

if __name__ == '__main__':
    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        'display.width', None,
        # 'display.max_colwidth', None,
    ):
        print(data_description)
