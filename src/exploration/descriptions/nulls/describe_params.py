from pandas import (
    # Index,
    MultiIndex,
)

descriptors = {
    ('type', ''): lambda _: _.dtypes,

    ('counts', ''): lambda _: _.apply(len),
    ('counts', 'null'): lambda _: _.isna().sum(),
    # ('counts', 'notnull'): lambda _: _.notna().sum(),
    ('counts', 'notnull'): lambda _: _.count(),

    ('portion', 'null'): lambda _: _.isna().sum() / _.shape[0],
    ('portion', 'notnull'): lambda _: _.count() / _.shape[0],
}

single_transformers = [
    lambda _: _[_[('counts', 'null')] != 0],

    lambda _: _.sort_values(
        by=[
            ('counts', 'null'),
            ('type', ''),
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
]

multi_transformers = [
    lambda _: _[
        (
            _[('counts', 'null', 'train')].notna() &
            _[('counts', 'null', 'train')] != 0
        ) |
        (
            _[('counts', 'null', 'test')].notna() &
            _[('counts', 'null', 'test')] != 0
        )
    ],

    (
        [
            ('counts', '', 'train'),
            ('counts', '', 'test'),
            ('counts', 'null', 'train'),
            ('counts', 'null', 'test'),
            ('counts', 'notnull', 'train'),
            ('counts', 'notnull', 'test'),
        ],
        lambda _: _.astype(int)
    ),

    lambda _: _.sort_values(
        by=[
            ('counts', 'null', 'train'),
            ('counts', 'null', 'test'),
            ('type', '', 'train'),
            ('type', '', 'test')
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
        mapper=('', '', 'dataset'),
        axis='columns',
    ),
]

single_params = dict(
    descriptors=descriptors,
    transformers=single_transformers,
)

multi_params = dict(
    descriptors=descriptors,
    inverse=True,
    transformers=multi_transformers,
)
