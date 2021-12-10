from typing import Callable, Any, Union
from pandas import DataFrame, Series, MultiIndex, concat


def describe(
    data: Union[DataFrame, dict[str, DataFrame]],
    descriptors: dict[Any, Callable[[DataFrame], Union[Series, Any]]],
    inverse: bool = False,
) -> DataFrame:
    if isinstance(data, DataFrame):
        descriptions = {
            description_key: descriptor(data)
            for description_key, descriptor in descriptors.items()
        }

        if all(
            [
                isinstance(description, Series)
                for description in descriptions.values()
            ]
        ):
            descriptions = DataFrame(descriptions)
        else:
            descriptions = Series(descriptions)
    elif (
        isinstance(data, dict) and
        all(
            [
                isinstance(data_set, DataFrame)
                for data_set in data.values()
            ]
        )
    ):
        descriptions = {
            data_key: {
                description_key: descriptor(data_set)
                for description_key, descriptor in descriptors.items()
            }
            for data_key, data_set in data.items()
        }

        if all(
            [
                all(
                    [
                        isinstance(description, Series)
                        for description in data_descriptions.values()
                    ]
                )
                for data_descriptions in descriptions.values()
            ]
        ):
            descriptions = concat(
                [
                    DataFrame(
                        {
                            (data_key, description_key): description
                            for description_key, description in data_descriptions.items()
                        }
                    )
                    for data_key, data_descriptions in descriptions.items()
                ],
                axis=1,
            )

            if inverse:
                descriptions = descriptions[
                    [
                        (data_key, description_key)
                        for description_key in descriptors.keys()
                        for data_key in data.keys()
                    ]
                ]

                descriptions.columns = MultiIndex.from_tuples(
                    [
                        descriptions_column[::-1]
                        for descriptions_column in descriptions.columns
                    ]
                )
        else:
            descriptions = DataFrame(descriptions)
    else:
        descriptions = None

    return descriptions
