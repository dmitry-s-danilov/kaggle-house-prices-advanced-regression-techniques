# from functools import partial

from ...tools import sample
from .params import n

# describe = partial(sample, n=n)


def describe(
    data,
    transformers=None,
):
    return sample(
        data=data,
        n=n,
        transformers=transformers,
    )
