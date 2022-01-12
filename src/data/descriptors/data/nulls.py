from typing import Union
from pandas import DataFrame

from ...descriptions import multi_keys
from ...descriptions.nulls import (
    describe as describe__,
    descriptors as descriptors__,
    single_transformers,
    multi_inverse, multi_keys_dependence, multi_transformers,
)


def describe(
    data: Union[DataFrame, dict],
    descriptors: dict = descriptors__,
    inverse: bool = False,
    transformers: Union[bool, list] = False,
) -> DataFrame:
    if transformers:
        if (
            isinstance(transformers, bool) and
            isinstance(data, DataFrame)
        ):
            params = dict(transformers=single_transformers)
        elif (
            isinstance(transformers, bool) and
            isinstance(data, dict) and
            set(data.keys()) == set(multi_keys) if multi_keys_dependence else True
        ):
            params = dict(
                inverse=multi_inverse,
                transformers=multi_transformers,
            )
        else:
            params = dict(
                inverse=inverse,
                transformers=transformers,
            )
    else:
        params = dict(inverse=inverse)

    return describe__(
        data=data,
        descriptors=descriptors,
        **params
    )
