from functools import partial

from ....data import load
from .. import describe
from .params import data_keys, descriptors


describe = partial(
    describe,
    data=load(data_keys=data_keys),
    descriptors=descriptors,
    transformers=None,
)
