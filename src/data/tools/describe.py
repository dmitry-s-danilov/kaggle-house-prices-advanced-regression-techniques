from typing import Callable, Union
from pandas import DataFrame, Series, MultiIndex, concat


def describe(
    data: Union[DataFrame, dict],
    descriptors: dict,
    inverse: bool = False,
) -> DataFrame:
    if (
        isinstance(data, DataFrame) and
        all(
            [
                isinstance(descriptor, Callable)
                for descriptor in descriptors.values()
            ]
        )
    ):
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
        ) and
        all(
            [
                isinstance(descriptor, Callable)
                for descriptor in descriptors.values()
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
                            (
                                (data_key, )
                                if not isinstance(data_key, tuple)
                                else data_key
                            ) +
                            (
                                (description_key, )
                                if not isinstance(description_key, tuple)
                                else description_key
                            ): description
                            for description_key, description in data_descriptions.items()
                        }
                    )
                    for data_key, data_descriptions in descriptions.items()
                ],
                axis=1,
            )

        if inverse:
            descriptions_keys = []
            descriptions_columns = []
            for description_key in descriptors.keys():
                for data_key in data.keys():
                    modified_data_key = (
                        (data_key, )
                        if not isinstance(data_key, tuple)
                        else data_key
                    )
                    modified_description_key = (
                        (description_key, )
                        if not isinstance(description_key, tuple)
                        else description_key
                    )
                    descriptions_keys.append(modified_data_key + modified_description_key)
                    descriptions_columns.append(modified_description_key + modified_data_key)
            descriptions = descriptions[descriptions_keys]
            descriptions.columns = MultiIndex.from_tuples(descriptions_columns)
        else:
            descriptions = DataFrame(descriptions)
    else:
        descriptions = None

    return descriptions
