from pandas import option_context
from .modified import description

with option_context(
    'display.max_rows', description.shape[0],
    'display.max_columns', description.shape[1],
    'display.width', None,
    # 'display.max_colwidth', None,
):
    print(description)
