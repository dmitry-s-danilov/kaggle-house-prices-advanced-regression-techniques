from functools import partial

from ....data import load
from .. import describe as main_describe
from .params import data_keys, descriptors, transformers

describe = partial(
    main_describe,
    data=load(data_keys=data_keys),
    descriptors=descriptors,
    transformers=transformers,
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
