from numpy import number
from pandas import (
    # Index,
    MultiIndex,
)

data_type = object

single_transformers = [
    lambda _: _.transpose(),

    lambda _: _.sort_values(
        by=['unique', 'count'],
        ascending=[True, False],
    ),

    # lambda _: _.set_index(enumerate(_.index, 1)),
    # lambda _: _.set_index(
    #     Index(
    #         data=enumerate(_.index, 1),
    #         name=('', 'variable'),
    #     ),
    # ),
    lambda _: _.set_index(
        MultiIndex.from_tuples(
            tuples=enumerate(_.index, 1),
            names=('', 'variable')
        )
    )
]
