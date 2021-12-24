from typing import Callable, Any, Union
from pandas import DataFrame


def transform(
    data,
    transformers: list[Union[Callable, tuple[Any, Callable], tuple[Any, Any, Callable]]],
):
    if isinstance(transformers, list):
        modified_data = data.copy()
        for transformer in transformers:
            if isinstance(transformer, Callable):
                modified_data = transformer(modified_data)
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 2 and
                isinstance(transformer[-1], Callable) and
                isinstance(modified_data, DataFrame)
            ):
                subset_key, subset_transformer = transformer
                modified_data[subset_key] = subset_transformer(modified_data[subset_key])
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 3 and
                isinstance(transformer[-1], Callable) and
                isinstance(modified_data, DataFrame)
            ):
                subset_key, modified_subset_key, subset_transformer = transformer
                modified_data[modified_subset_key] = subset_transformer(modified_data[subset_key])
            else:
                modified_data = None
                break
    else:
        modified_data = None
    return modified_data
