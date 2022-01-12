from typing import Callable, Union
from pandas import DataFrame

from ...tools import (
    sample as sample__,
    transform,
)
from .params import n as n__


def sample(
    data: DataFrame,
    n: Union[int, tuple] = n__,
    transformers: list = None,
) -> DataFrame:
    return transform(
        data=sample__(
            data=data,
            n=n,
        ),
        transformers=transformers,
    )
