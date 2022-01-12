#!/bin/python

from contest.data.sets import load

data_key = 'train'

if __name__ == '__main__':
    data_set = load(data_key, info=True)
