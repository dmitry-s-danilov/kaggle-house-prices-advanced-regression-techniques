#!/bin/python

from subprocess import run

interpreter = 'python'
module = 'contest.utils.merge_notebooks'

input_paths = [
    '0-head.ipynb',
    '1-variables.ipynb',
    '2-datasets.ipynb',
    '3-dataset-1-train.ipynb',
    # '3-dataset-2-test.ipynb',
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
