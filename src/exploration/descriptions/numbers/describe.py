from ...tools import transform
from .params import data_type


def describe(
    data,
    transformers=None,
):
    return transform(
        data=data.select_dtypes(data_type).describe(),
        transformers=transformers,
    )
