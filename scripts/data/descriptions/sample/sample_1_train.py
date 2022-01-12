#!/bin/python

from pandas import option_context

from contest.data.sets import load
from contest.data.descriptions.sample import sample, transformers

key = 'train'

if __name__ == '__main__':
    data = load(key)
    sample_ = sample(data, transformers=transformers)

    with option_context(
        'display.max_rows', sample_.shape[0],
        'display.max_columns', sample_.shape[1],
        # 'display.max_colwidth', None,
        'display.width', None,
    ):
        print(sample_)
