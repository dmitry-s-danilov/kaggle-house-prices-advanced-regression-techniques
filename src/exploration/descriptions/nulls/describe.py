# from functools import partial

from ...tools import describe as main_describe
from .params import descriptors

# describe = partial(main_describe, descriptors=descriptors)


def describe(
    data,
    inverse=False,
    transformers=None,
):
    return main_describe(
        data=data,
        descriptors=descriptors,
        inverse=inverse,
        transformers=transformers,
    )


if __name__ == '__main__':
    from pandas import option_context

    from ....data import load
    from ..params import default_data_keys as data_keys
    from .params import default_multi_params as describe_params

    data_sets = load(data_keys)
    data_description = describe(data_sets, **describe_params)

    with option_context(
        'display.max_rows', data_description.shape[0],
        'display.max_columns', data_description.shape[1],
        'display.width', None,
    ):
        print(data_description)
