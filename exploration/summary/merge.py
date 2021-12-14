#!/bin/python

from subprocess import run

interpreter = 'python'
module = 'contest.utils.merge_notebooks'

input_paths = [
    'head.ipynb',
    'info.ipynb',
    'types.ipynb',
    'nulls.ipynb',
    'uniques.ipynb',
    'train.ipynb',
    # 'test.ipynb',
]
output_path = 'summary.ipynb'

args = [
    interpreter,
    '-m', module,
    '--input_paths', *input_paths,
    '--output_path', output_path,
]

if __name__ == '__main__':
    run(args)

