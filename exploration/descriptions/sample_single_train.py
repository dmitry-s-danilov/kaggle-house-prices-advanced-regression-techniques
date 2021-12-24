#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.tools import sample, transform
from contest.exploration.descriptions.sample import transform_transformers as transformers

data_key = 'train'
n = 3, 6, 3

if __name__ == '__main__':
    description = transform(
        data=sample(
            data=load(data_keys=data_key),
            n=n,
        ),
        transformers=transformers
    )

    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        'display.width', None,
    ):
        print(description)
