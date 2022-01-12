#!/bin/python

from contest.data.sets import load

data_keys = ['train', 'test']

if __name__ == '__main__':
    data_sets = load(data_keys, info=True)
