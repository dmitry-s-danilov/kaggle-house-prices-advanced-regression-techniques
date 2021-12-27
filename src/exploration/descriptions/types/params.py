from numpy import number

descriptors = {
    ('shape', 'rows', '', ''): lambda _: _.shape[0],
    ('shape', 'columns', '', ''): lambda _: _.shape[1],

    # # # ('shape', 'columns', 'nulls', ''): lambda _: _.isna().values.any(),
    # ('shape', 'columns', 'nulls', ''): lambda _: _.isna().any().any(),
    # # # ('shape', 'columns', 'non-nulls', ''): lambda _: _.notna().values.all(),
    # ('shape', 'columns', 'non-nulls', ''): lambda _: _.notna().all().all(),

    ('shape', 'columns', '', False): lambda _: _.notna().all().sum(),
    ('shape', 'columns', '', True): lambda _: _.isna().any().sum(),

    ('type', object, '', ''): lambda _: _.select_dtypes(object).shape[1],
    ('type', object, '', False): lambda _: _.select_dtypes(object).notna().all().sum(),
    ('type', object, '', True): lambda _: _.select_dtypes(object).isna().any().sum(),

    # ('type', number, '', ''): lambda _: _._get_numeric_data().shape[1],
    ('type', number, '', ''): lambda _: _.select_dtypes(number).shape[1],
    ('type', number, '', False): lambda _: _.select_dtypes(number).notna().all().sum(),
    ('type', number, '', True): lambda _: _.select_dtypes(number).isna().any().sum(),

    ('type', number, int, ''): lambda _: _.select_dtypes(int).shape[1],
    ('type', number, int, False): lambda _: _.select_dtypes(int).notna().all().sum(),
    ('type', number, int, True): lambda _: _.select_dtypes(int).isna().any().sum(),

    ('type', number, float, ''): lambda _: _.select_dtypes(float).shape[1],
    ('type', number, float, False): lambda _: _.select_dtypes(float).notna().all().sum(),
    ('type', number, float, True): lambda _: _.select_dtypes(float).isna().any().sum(),
}

single_transformers = [
    lambda _: _.rename_axis(
        mapper=('', '', '', 'detect nulls'),
        axis='index',
    )
]

default_multi_transformers = [
    lambda _: _.rename_axis(
        mapper=('', '', '', 'detect nulls'),
        axis='index',
    ),

    lambda _: _.rename_axis(
        mapper='dataset',
        axis='columns',
    ),
]

default_multi_params = dict(transformers=default_multi_transformers)
