#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.tools import transform
from contest.exploration.descriptions.objects import transform_transformers as transformers

data_key = 'test'
data_type = object

if __name__ == '__main__':
    data_set = load(data_keys=data_key)
    data_description = transform(
        data=data_set.select_dtypes(data_type).describe(),
        transformers=transformers,
    )

    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        'display.width', None,
    ):
        print(data_description)
