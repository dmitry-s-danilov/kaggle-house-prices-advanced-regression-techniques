#!/bin/python

from pandas import option_context

from contest.data.sets import load
from contest.data.descriptions.nulls import (
    describe,
    single_transformers as transformers,
)

key = 'train'

if __name__ == '__main__':
    data = load(key)
    description = describe(data, transformers=transformers)

    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        # 'display.max_colwidth', None,
        'display.width', None,
    ):
        print(description)
