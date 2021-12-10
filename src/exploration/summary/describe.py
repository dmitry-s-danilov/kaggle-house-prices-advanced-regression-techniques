from typing import Callable, Any, Union
from pandas import DataFrame, Series

from ..tools import (
    describe as primary_describe,
    transform,
)


def describe(
    data: Union[DataFrame, dict[Any, DataFrame]],
    descriptors: dict[Any, Callable[[DataFrame], Union[Series, Any]]],
    transformers: list[
        Union[
            Callable[[Union[Series, DataFrame]], Union[Series, DataFrame]],
            tuple[Any, Callable[[Union[Series, DataFrame]], Union[Series, DataFrame]]],
        ]
    ] = None,
) -> DataFrame:
    primary_transformers = [
        lambda _: primary_describe(
            data=_,
            descriptors=descriptors,
            inverse=True,
        ),
    ]
    if transformers is not None:
        primary_transformers.append(
            lambda _: transform(
                data=_,
                transformers=transformers,
            )
        )

    return transform(
        data=data,
        transformers=primary_transformers,
    )
