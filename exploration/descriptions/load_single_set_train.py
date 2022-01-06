#!/bin/python

from contest.data import load

load_params = dict(
    data_keys='train',
    print_info=True
)

if __name__ == '__main__':
    data_set = load(**load_params)
