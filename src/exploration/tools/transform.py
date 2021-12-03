from typing import Callable, Any, Union
from pandas import DataFrame, Series


def transform(
    data: DataFrame,
    transformers: list[
        Union[
            Callable[
                [Union[Series, DataFrame]],
                Union[Series, DataFrame]
            ],
            tuple[
                Any,
                Callable[
                    [Union[Series, DataFrame]],
                    Union[Series, DataFrame]
                ]
            ],
        ]
    ],
) -> DataFrame:
    if isinstance(transformers, list):
        data_transformed = data.copy()
        for transformer in transformers:
            if isinstance(transformer, Callable):
                data_transformed = transformer(data_transformed)
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 2 and
                isinstance(transformer[1], Callable)
            ):
                sub_key, sub_transformer = transformer
                data_transformed[sub_key] = sub_transformer(data_transformed[sub_key])
            else:
                data_transformed = None
                break
    else:
        data_transformed = None
    return data_transformed
