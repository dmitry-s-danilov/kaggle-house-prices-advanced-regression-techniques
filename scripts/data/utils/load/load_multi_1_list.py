#!/bin/python

from contest.data.utils import load
from contest.data.sets import paths as data_paths

data_keys = ['train', 'test']

if __name__ == '__main__':
    data_paths_ = [
        data_path
        for data_key, data_path in data_paths.items()
        if data_key in data_keys
    ]
    data_sets = load(data_paths_, info=True)
