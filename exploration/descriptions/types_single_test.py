#!/bin/python

from pandas import option_context

from contest.data import load
from contest.exploration.descriptions.types import (
    describe,
    single_transformers as describe_transformers,
)

data_key = 'test'

if __name__ == '__main__':
    data_set = load(data_key)
    data_description = describe(
        data=data_set,
        transformers=describe_transformers,
    )

    with option_context(
        'display.max_rows', len(data_description),
        'display.width', None,
    ):
        print(data_description)
