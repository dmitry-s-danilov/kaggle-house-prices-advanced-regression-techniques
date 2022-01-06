#!/bin/python

from contest.data import load

load_params = dict(
    data_keys=['train', 'test'],
    print_info=True,
)

if __name__ == '__main__':
    data_sets = load(**load_params)