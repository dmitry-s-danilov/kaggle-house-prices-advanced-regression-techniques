from pandas import DataFrame

from .description import description as description__
from .params import (
    construct_params as params__,
    construct_index_params as index_params__,
)


def construct(
    data: dict = description__,
    params: dict = params__,
    index_params: dict = index_params__,
) -> DataFrame:
    return DataFrame.from_dict(data, **params).set_index(**index_params)
