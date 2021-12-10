from typing import Callable, Any, Union
from pandas import DataFrame, Series


def transform(
    data: Union[DataFrame, dict[Any, DataFrame]],
    transformers: list[
        Union[
            Callable[
                [Union[Series, DataFrame, dict[Any, DataFrame]]],
                Union[Series, DataFrame],
            ],
            tuple[
                Any,
                Callable[
                    [Union[Series, DataFrame]],
                    Union[Series, DataFrame],
                ],
            ],
        ]
    ],
) -> DataFrame:
    if isinstance(transformers, list):
        transformed_data = data.copy()
        for transformer in transformers:
            if isinstance(transformer, Callable):
                transformed_data = transformer(transformed_data)
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 2 and
                isinstance(transformer[1], Callable)
            ):
                subset_key, subset_transformer = transformer
                transformed_data[subset_key] = subset_transformer(transformed_data[subset_key])
            else:
                transformed_data = None
                break
    else:
        transformed_data = None
    return transformed_data
