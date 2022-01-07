from typing import Union
from pandas import DataFrame

from .spec import data_spec as default_data_spec
from .params import index_params


def describe(
    data_spec: dict = default_data_spec,
    var_type: Union[tuple[str], str] = None,
) -> DataFrame:
    data_description = DataFrame(data_spec).set_index(**index_params)

    if isinstance(var_type, tuple) and len(var_type) == 2:
        data_description = data_description[
            data_description['type'] == var_type
        ]
    elif isinstance(var_type, str):
        data_description = data_description[
            data_description['type'].apply(lambda _: var_type in _)
        ]

    return data_description
