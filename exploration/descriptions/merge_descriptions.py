#!/bin/python

from subprocess import run

interpreter = 'python'
module = 'contest.utils.merge_notebooks'

input_paths = [
    '0-head.ipynb',
    '1-data_variables.ipynb',
    '2-multi_set.ipynb',
    '3_1-single_set-train.ipynb',
    # '3_2-single_set-test.ipynb',
]
output_path = '4-merged.ipynb'

args = [
    interpreter,
    '-m', module,
    '--input_paths', *input_paths,
    '--output_path', output_path,
]

if __name__ == '__main__':
    run(args)
