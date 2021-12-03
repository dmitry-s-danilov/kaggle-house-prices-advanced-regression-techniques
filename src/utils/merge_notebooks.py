from argparse import ArgumentParser
from json import load, dump

load_params = dict(
    mode='r',
    encoding='utf-8',
)

dump_params = dict(
    mode='w',
    encoding='utf-8',
)

cells_key = 'cells'

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-i', '--input_paths',
        type=str, nargs='+',
    )
    parser.add_argument(
        '-o', '--output_path',
        type=str
    )

    args = parser.parse_args()
    input_paths = args.input_paths
    output_path = args.output_path

    input_notebooks = []
    for input_path in input_paths:
        with open(input_path, **load_params) as file:
            input_notebooks.append(load(file))

    output_notebook = input_notebooks[0].copy()
    for input_notebook in input_notebooks[1:]:
        output_notebook[cells_key] += input_notebook[cells_key]

    with open(output_path, **dump_params) as file:
        dump(output_notebook, file)
