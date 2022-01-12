#!/bin/python

from contest.data.sets import load

data_key = 'test'

if __name__ == '__main__':
    data_set = load(data_key, info=True)

