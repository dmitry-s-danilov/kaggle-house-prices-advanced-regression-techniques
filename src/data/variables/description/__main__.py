#!/bin/python

from pandas import option_context
from .construct import construct

description = construct()

with option_context(
    'display.max_rows', description.shape[0],
    'display.max_columns', description.shape[1],
    # 'display.max_colwidth', None,
    'display.width', None,
):
    print(description)
