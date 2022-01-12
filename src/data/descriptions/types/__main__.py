from pandas import option_context

from ...sets import load
from .describe import describe
from ..params import multi_keys as keys
from .params import (
    multi_inverse as inverse,
    multi_transformers as transformers,
)

data = load(keys)
description = describe(
    data,
    inverse=inverse,
    transformers=transformers,
)

with option_context(
    'display.max_rows', description.shape[0],
    'display.max_columns', description.shape[1],
    # 'display.max_colwidth', None,
    'display.width', None,
):
    print(description)
