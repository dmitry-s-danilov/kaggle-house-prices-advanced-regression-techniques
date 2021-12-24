#!/bin/python

from contest.data import load

load_params = dict(
    data_keys='test',
    print_info=True
)

if __name__ == '__main__':
    load(**load_params)
