from pandas import DataFrame

from .vars_raw import vars_description as raw_vars_description
from .vars_params import index_params

vars_description = DataFrame(
    raw_vars_description
).set_index(
    **index_params
)
