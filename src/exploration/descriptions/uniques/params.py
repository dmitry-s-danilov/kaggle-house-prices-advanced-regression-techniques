from pandas import (
    # Index,
    MultiIndex,
)

descriptors = {
    ('type', '', ''): lambda _: _.dtypes,

    ('counts', '', ''): lambda _: _.apply(len),
    ('counts', 'non-null', ''): lambda _: _.count(),
    ('counts', 'null', ''): lambda _: _.isna().sum(),

    ('unique', 'counts', True): lambda _: _.nunique(dropna=False),
    ('unique', 'counts', False): lambda _: _.nunique(),

    ('unique', 'ratio', True): lambda _: _.nunique(dropna=False) / _.shape[0],
    ('unique', 'ratio', False): lambda _: _.nunique() / _.count(),
}

single_transformers = [
    # lambda _: _.dropna(),
    lambda _: _[
        _[
            ('unique', 'ratio', False)
        ].notna()
    ],

    lambda _: _.sort_values(
        by=[
            ('unique', 'counts', True),
            ('unique', 'counts', False),
            ('counts', 'null', ''),
            ('type', '', ''),
        ]
    ),

    # lambda _: _.set_index(enumerate(_.index, 1)),
    # lambda _: _.set_index(
    #     Index(
    #         data=enumerate(_.index, 1),
    #         name=('', 'variable'),
    #     ),
    # ),
    lambda _: _.set_index(
        MultiIndex.from_tuples(
            tuples=enumerate(_.index, 1),
            names=('', 'variable')
        )
    ),

    lambda _: _.rename_axis(
        mapper=('', '', 'include nulls'),
        axis='columns',
    ),
]

default_multi_transformers = [
    # lambda _: _.dropna(),
    lambda _: _[
        _[
            [
                ('counts', '', '', 'train'),
                ('counts', '', '', 'test'),
                ('counts', 'non-null', '', 'train'),
                ('counts', 'non-null', '', 'test'),
                ('counts', 'null', '', 'train'),
                ('counts', 'null', '', 'test'),
                ('unique', 'counts', True, 'train'),
                ('unique', 'counts', True, 'test'),
                ('unique', 'counts', False, 'train'),
                ('unique', 'counts', False, 'test'),
                ('unique', 'ratio', False, 'train'),
                ('unique', 'ratio', False, 'test'),
            ]
        ].notna().all(axis=1)
    ],

    (
        [
            ('counts', '', '', 'train'),
            ('counts', '', '', 'test'),
            ('counts', 'non-null', '', 'train'),
            ('counts', 'non-null', '', 'test'),
            ('counts', 'null', '', 'train'),
            ('counts', 'null', '', 'test'),
            ('unique', 'counts', True, 'train'),
            ('unique', 'counts', True, 'test'),
            ('unique', 'counts', False, 'train'),
            ('unique', 'counts', False, 'test'),
        ],
        lambda _: _.astype(int)
    ),

    lambda _: _.sort_values(
        by=[
            ('unique', 'counts', True, 'train'),
            ('unique', 'counts', True, 'test'),
            ('unique', 'counts', False, 'train'),
            ('unique', 'counts', False, 'test'),
            ('counts', 'null', '', 'train'),
            ('counts', 'null', '', 'test'),
            ('type', '', '', 'train'),
            ('type', '', '', 'test'),
        ]
    ),

    # lambda _: _.set_index(enumerate(_.index, 1)),
    # lambda _: _.set_index(
    #     Index(
    #         data=enumerate(_.index, 1),
    #         name=('', 'variable'),
    #     )
    # ),
    lambda _: _.set_index(
        MultiIndex.from_tuples(
            tuples=enumerate(_.index, 1),
            names=('', 'variable'),
        )
    ),

    lambda _: _.rename_axis(
        mapper=('', '', 'include nulls', 'dataset'),
        axis='columns',
    ),
]

default_multi_params = dict(
    inverse=True,
    transformers=default_multi_transformers,
)
