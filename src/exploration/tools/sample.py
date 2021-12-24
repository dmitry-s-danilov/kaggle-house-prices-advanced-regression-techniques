from pandas import DataFrame, concat


def sample(
    data: DataFrame,
    n: tuple[int, int, int] = (5, 5, 5),
) -> DataFrame:
    return concat(
        [
            data.iloc[:n[0], :],  # data.head(n[0]),
            data.iloc[n[0]: -n[-1], :].sample(n[1]).sort_index(),
            data.iloc[-n[-1]:, :],  # data.tail(n[-1]),
        ]
    ) if (
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
    ) else None
