#!/bin/python

from subprocess import run

interpreter = 'python'
module = 'contest.utils.merge_notebooks'

input_paths = [
    'description_0_head.ipynb',
    'description_1_multi.ipynb',
    'description_2_1_single_train.ipynb',
    # 'description_2_2_single_test.ipynb',
]
output_path = 'description_3_merged.ipynb'

args = [
    interpreter,
    '-m', module,
    '--input_paths', *input_paths,
    '--output_path', output_path,
]

if __name__ == '__main__':
    run(args)
