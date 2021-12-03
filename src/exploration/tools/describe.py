from typing import Callable, Any, Union
from pandas import DataFrame, Series, MultiIndex, concat


def describe(
    data: Union[DataFrame, dict[Any, DataFrame]],
    descriptors: dict[Any, Callable[[DataFrame], Union[Series, Any]]],
    inverse: bool = False,
) -> DataFrame:
    if isinstance(data, DataFrame):
        data_descriptions = {
            descriptor_key: descriptor(data)
            for descriptor_key, descriptor in descriptors.items()
        }

        if all(
            [
                isinstance(description_value, Series)
                for description_value in data_descriptions.values()
            ]
        ):
            data_descriptions = DataFrame(data_descriptions)
        else:
            data_descriptions = Series(data_descriptions)

    elif (
        isinstance(data, dict) and
        all(
            [
                isinstance(data_set, DataFrame)
                for data_set in data.values()
            ]
        )
    ):
        data_descriptions = {
            data_key: {
                descriptor_key: descriptor(data_set)
                for descriptor_key, descriptor in descriptors.items()
            }
            for data_key, data_set in data.items()
        }

        if all(
            [
                all(
                    [
                        isinstance(description_value, Series)
                        for description_value in data_description.values()
                    ]
                )
                for data_description in data_descriptions.values()
            ]
        ):
            data_descriptions = concat(
                [
                    DataFrame(
                        {
                            (data_key, description_key): description_value
                            for description_key, description_value in data_description.items()
                        }
                    )
                    for data_key, data_description in data_descriptions.items()
                ],
                axis=1,
            )
        else:
            data_descriptions = DataFrame(data_descriptions)

        if inverse:
            data_descriptions = data_descriptions[
                [
                    (data_key, descriptor_key)
                    for descriptor_key in descriptors.keys()
                    for data_key in data.keys()
                ]
            ]
            data_descriptions.columns = MultiIndex.from_tuples(
                [
                    description_column[::-1]
                    for description_column in data_descriptions.columns
                ]
            )
    else:
        data_descriptions = None

    return data_descriptions
