from typing import Callable, Any, Union
from pandas import DataFrame

from ....data import (
    data_spec as default_data_spec,
    describe as main_describe
)
from ...tools import transform
from .params import (
    transformers as default_transformers,
    var_type as main_var_type,
)


def describe(
    data_spec: dict = default_data_spec,
    transformers: list[Union[Callable, tuple[Any, Callable], tuple[Any, Any, Callable]]] = default_transformers,
) -> DataFrame:
    return transform(
        data=main_describe(
            data_spec=data_spec,
            var_type=main_var_type,
        ),
        transformers=transformers,
    )
