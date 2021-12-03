from pandas import DataFrame

from ....data import load
from ...tools import describe, transform

default_data_keys = ['train', 'test']

descriptors = {
    # 'total counts': lambda _: _.apply(len),
    'unique counts': lambda _: _.nunique(),
    'unique portion': lambda _: _.nunique() / _.shape[0],
    'null': lambda _: _.isna().any(),
    'type': lambda _: _.dtypes,
}

transformers = [
    lambda _: _.dropna(),

    lambda _: _.sort_values(
        by=[
            ('unique counts', 'train'),
            ('unique counts', 'test'),
            ('null', 'train'),
            ('null', 'test'),
        ]
    ),

    lambda _: _.reset_index().rename(
        columns={'index': 'variable'}
    ),

    # (
    #     [
    #         ('total counts', 'train'),
    #         ('total counts', 'test'),
    #         ('unique counts', 'train'),
    #         ('unique counts', 'test'),
    #     ],
    #     lambda _: _.astype(int)
    # )
    ('unique counts', lambda _: _.astype(int))
]


def customized_describe(data: dict[str, DataFrame] = None) -> DataFrame:
    modified_data = load(data_keys=default_data_keys) if data is None else data

    description = describe(
        modified_data,
        descriptors,
        inverse=True,
    )
    description = transform(
        description,
        transformers,
    )

    return description
