from pandas import DataFrame

from ....data import load
from ...tools import describe, transform

default_data_keys = ['train', 'test']

descriptors = {
    # 'total counts': lambda _: _.apply(len),

    'null counts': lambda _: _.isna().sum(),
    'null portion': lambda _: _.isna().sum() / _.shape[0],

    # # 'notnull counts': lambda _: _.notna().sum(),
    # 'notnull counts': lambda _: _.count(),
    # 'notnull portion': lambda _: _.count() / _.shape[0],

    'type': lambda _: _.dtypes,
}

transformers = [
    lambda _: _[
        (
            (_['null counts'] != 0) &
            _['null counts'].notna()
        ).any(axis=1)
    ],

    lambda _: _.sort_values(
        by=[
            ('null counts', 'train'),
            ('null counts', 'test'),
        ]
    ),

    lambda _: _.reset_index().rename(
        columns={'index': 'variable'}
    ),

    # (
    #     [
    #         ('total counts', 'train'),
    #         ('total counts', 'test'),
    #         ('null counts', 'train'),
    #         ('null counts', 'test'),
    #         ('notnull counts', 'train'),
    #         ('notnull counts', 'test'),
    #     ],
    #     lambda _: _.astype(int)
    # ),
    ('null counts', lambda _: _.astype(int)),
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
