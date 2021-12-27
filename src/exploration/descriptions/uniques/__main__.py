from pandas import option_context

from ....data import load
from ..params import default_data_keys as data_keys
from .describe import describe
from .params import default_multi_params as describe_params

data_sets = load(data_keys)
data_description = describe(data_sets, **describe_params)

with option_context(
    'display.max_rows', data_description.shape[0],
    'display.max_columns', data_description.shape[1],
    'display.width', None,
):
    print(data_description)
