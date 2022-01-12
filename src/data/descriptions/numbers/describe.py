from typing import Callable, Union
from pandas import DataFrame

from ...tools import transform
from .params import dtype


def describe(
    data: DataFrame,
    transformers: list[Union[Callable, tuple]] = None,
):
    return transform(
        data=data.select_dtypes(dtype).describe(),
        transformers=transformers,
    )
