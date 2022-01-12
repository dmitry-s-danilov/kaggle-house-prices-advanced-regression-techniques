from typing import Union
from pandas import DataFrame

from ...descriptions.sample import (
    sample as sample__,
    n as n__,
    transformers as transformers__,
)

def sample(
    data: [DataFrame, dict],
    n: Union[int, tuple] = n__,
    transformers: list = False,
) -> [DataFrame, dict]:
    pass
