from typing import Union
from pandas import DataFrame

from ...tools import (
    describe as describe__,
    transform,
)
from .params import descriptors as descriptors__


def describe(
    data: Union[DataFrame, dict],
    descriptors: dict = descriptors__,
    inverse: bool = False,
    transformers: list = None,
) -> DataFrame:
    return transform(
        data=describe__(
            data=data,
            descriptors=descriptors,
            inverse=inverse,
        ),
        transformers=transformers,
    )
