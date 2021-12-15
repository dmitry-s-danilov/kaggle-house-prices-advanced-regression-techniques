from copy import deepcopy

keys = dict(
    cells='cells',
    cell_id='id',
)


def merge(notebooks: list[dict]) -> dict:
    separate_notebooks = [
        deepcopy(notebook)
        for notebook in notebooks
    ]

    for notebook in separate_notebooks:
        for cell in notebook[keys['cells']]:
            del cell[keys['cell_id']]

    combined_notebook = deepcopy(separate_notebooks[0])
    for notebook in separate_notebooks[1:]:
        combined_notebook[keys['cells']] += notebook[keys['cells']]

    return combined_notebook
