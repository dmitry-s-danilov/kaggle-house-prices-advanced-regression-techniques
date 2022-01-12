from pandas import option_context

from ...sets import load
from .sample import sample
from ..params import multi_keys as keys
from .params import transformers

datasets = load(keys)
samples = {
    key: sample(dataset, transformers=transformers)
    for key, dataset in datasets.items()
}

for key, sample_ in samples.items():
    with option_context(
        'display.max_rows', sample_.shape[0],
        'display.max_columns', sample_.shape[1],
        # 'display.max_colwidth', None,
        'display.width', None,
    ):
        print(key, sample_, sep=':\n')
