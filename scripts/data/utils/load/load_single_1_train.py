#!/bin/python

from contest.data.utils import load
from contest.data.sets import paths as data_paths

data_key = 'train'

if __name__ == '__main__':
    data_path = data_paths[data_key]
    data_set = load(data_path, info=True)
