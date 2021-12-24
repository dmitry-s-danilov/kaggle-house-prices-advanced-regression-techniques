from pandas import option_context
from .describe import describe

description = describe()

with option_context(
        'display.max_rows', description.shape[0],
        'display.max_columns', description.shape[1],
        'display.width', None,
):
    print(description)
