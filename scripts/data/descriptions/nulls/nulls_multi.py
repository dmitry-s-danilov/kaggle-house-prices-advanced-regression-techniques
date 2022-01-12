#!/bin/python

from pandas import option_context

from contest.data.sets import load
from contest.data.descriptions import multi_keys as keys
from contest.data.descriptions.nulls import (
    describe,
    multi_inverse as inverse,
    multi_transformers as transformers,
)

data = load(keys)
description = describe(
    data,
    inverse=inverse,
    transformers=transformers,
)

with option_context(
    'display.max_rows', description.shape[0],
    'display.max_columns', description.shape[1],
    # 'display.max_colwidth', None,
    'display.width', None,
):
    print(description)
