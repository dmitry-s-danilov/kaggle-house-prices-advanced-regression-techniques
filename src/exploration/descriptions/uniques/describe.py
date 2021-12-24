from ....data import load
from ...tools import describe as main_describe
from ..describe_params import multi_keys
from .describe_params import multi_params


def describe():
    return main_describe(
        data=load(data_keys=multi_keys),
        **multi_params
    )


if __name__ == '__main__':
    from pandas import option_context

    description = describe()

    with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        'display.width', None,
    ):
        print(description)
