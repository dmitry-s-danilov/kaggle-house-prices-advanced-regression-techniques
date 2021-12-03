from numpy import number
from pandas import DataFrame

from ....data import load
from ...tools import describe, transform

default_data_keys = ['train', 'test']

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


def customized_describe(data: dict[str, DataFrame] = None) -> DataFrame:
    modified_data = load(data_keys=default_data_keys) if data is None else data

    description = describe(
        modified_data,
        descriptors,
    )

    return description
