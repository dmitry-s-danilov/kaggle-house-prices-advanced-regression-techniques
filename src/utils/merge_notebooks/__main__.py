from argparse import ArgumentParser
from json import load, dump

from .params import load_params, dump_params
from .merge import merge, keys

parser = ArgumentParser()
parser.add_argument(
    '-i', '--input_paths',
    type=str, nargs='+',
)
parser.add_argument(
    '-o', '--output_path',
    type=str,
)

args = parser.parse_args()
input_paths = args.input_paths
output_path = args.output_path

input_notebooks = []
for input_path in input_paths:
    with open(input_path, **load_params) as file:
        input_notebooks.append(load(file))
        print(f"load {input_path} - cells: {len(input_notebooks[-1][keys['cells']])}")

output_notebook = merge(input_notebooks)

with open(output_path, **dump_params) as file:
    dump(output_notebook, file)
    print(f"dump {output_path} - cells: {len(output_notebook[keys['cells']])}")
