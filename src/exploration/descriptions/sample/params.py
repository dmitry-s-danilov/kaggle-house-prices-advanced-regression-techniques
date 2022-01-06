from pandas import (
    # Index,
    MultiIndex,
)

n = (3, 6, 3)

single_transformers = [
    lambda _: _.transpose(),

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
    ),

    lambda _: _.rename_axis(
        mapper='id',
        axis='columns',
    ),
]