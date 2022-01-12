from pandas import option_context

from ...sets import load
from .describe import describe
from ..params import multi_keys as keys
from .params import transformers

datasets = load(keys)
descriptions = {
    key: describe(dataset, transformers=transformers)
    for key, dataset in datasets.items()
}

for key, description in descriptions.items():
    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        # 'display.max_colwidth', None,
        'display.width', None,
    ):
        print(key, description, sep=':\n')
