from pandas import DataFrame

from .raw import description as raw_description
from .params import index_params

description = DataFrame(
    raw_description
).set_index(
    **index_params
)
