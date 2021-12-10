data_keys = ['train', 'test']

descriptors = {
    # 'total counts': lambda _: _.apply(len),
    'unique counts': lambda _: _.nunique(),
    'unique portion': lambda _: _.nunique() / _.shape[0],
    'null': lambda _: _.isna().any(),
    'type': lambda _: _.dtypes,
}

transformers = [
    lambda _: _.dropna(),

    # (
    #     [
    #         ('total counts', 'train'),
    #         ('total counts', 'test'),
    #         ('unique counts', 'train'),
    #         ('unique counts', 'test'),
    #     ],
    #     lambda _: _.astype(int)
    # )
    ('unique counts', lambda _: _.astype(int)),

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
]
