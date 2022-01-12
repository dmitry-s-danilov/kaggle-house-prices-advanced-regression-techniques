from typing import Union
from pandas import DataFrame

from .types import describe as describe_types
from .nulls import describe as describe_nulls
from .uniques import describe as describe_uniques


class DataDescriptor:
    def __init__(self, data: Union[DataFrame, dict]):
        self.data = data

    def types(self, *args, **kwargs):
        return describe_types(self.data, *args, **kwargs)

    def nulls(self, *args, **kwargs):
        return describe_nulls(self.data, *args, **kwargs)

    def uniques(self, *args, **kwargs):
        return describe_uniques(self.data, *args, **kwargs)
