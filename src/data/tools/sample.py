from typing import Union
from pandas import DataFrame, concat


def sample(
    data: DataFrame,
    n: Union[int, tuple[int]] = 1,
) -> DataFrame:
    if (
        isinstance(data, DataFrame) and
        isinstance(n, int) and
        n >= 0
    ):
        sample_ = data.sample(n).sort_index()
    elif (
        isinstance(data, DataFrame) and
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
        sample_ = concat(
            [
                # data.head(n[0]),
                data.iloc[:n[0], :],
                data.iloc[n[0]: -n[-1], :].sample(n[1]).sort_index(),
                # data.tail(n[-1]),
                data.iloc[-n[-1]:, :],
            ]
        )
    else:
        sample_ = None

    return sample_
