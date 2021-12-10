from numpy import number

data_keys = ['train', 'test']

descriptors = {
    'rows': lambda _: _.shape[0],
    'columns': lambda _: _.shape[1],

    'object': lambda _: _.select_dtypes(object).shape[1],
    # 'number': lambda _: _._get_numeric_data().shape[1],
    'number': lambda _: _.select_dtypes(number).shape[1],

    'int': lambda _: _.select_dtypes(int).shape[1],
    'float': lambda _: _.select_dtypes(float).shape[1],

    'null': lambda _: _.isna().values.any(),
    # 'notnull': lambda _: _.notna().values.all(),
}
