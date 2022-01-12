from typing import Callable, Union


def transform(
    data,
    transformers: list[Union[Callable, tuple]],
):
    data_ = data.copy()
    
    if isinstance(transformers, list):
        for transformer in transformers:
            if isinstance(transformer, Callable):
                data_ = transformer(data_)
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 2 and
                isinstance(transformer[-1], Callable) and
                hasattr(data, '__getitem__')
            ):
                key, transformer = transformer
                data_[key] = transformer(data_[key])
            elif (
                isinstance(transformer, tuple) and
                len(transformer) == 3 and
                isinstance(transformer[-1], Callable) and
                hasattr(data, '__getitem__')
            ):
                key, key_, transformer = transformer
                data_[key_] = transformer(data_[key])
            else:
                continue
    
    return data_
