from typing import Callable, Any, Union
from pandas import DataFrame, concat

from .transform import transform


def sample(
    data: DataFrame,
    n: tuple[int, int, int] = (5, 5, 5),
    transformers: list[Union[Callable, tuple[Any, Callable], tuple[Any, Any, Callable]]] = None,
) -> DataFrame:
    if transformers is None:
        if (
            isinstance(n, tuple) and
            len(n) == 3 and
            all(
                [
                    (
                            isinstance(_, int) and
                            _ >= 0
                    )
                    for _ in n
                ]
            )
        ):
            data_sample = concat(
                [
                    # data.head(n[0]),
                    data.iloc[:n[0], :],
                    data.iloc[n[0]: -n[-1], :].sample(n[1]).sort_index(),
                    # data.tail(n[-1]),
                    data.iloc[-n[-1]:, :],
                ]
            )
        else:
            data_sample = None
    else:
        data_sample = transform(
            data=sample(
                data=data,
                n=n,
            ),
            transformers=transformers,
        )

    return data_sample
