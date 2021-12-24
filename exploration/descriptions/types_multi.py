#!/bin/python

from pandas import option_context
from contest.exploration.descriptions.types import describe

if __name__ == '__main__':
    description = describe()

    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        'display.width', None,
    ):
        print(description)
