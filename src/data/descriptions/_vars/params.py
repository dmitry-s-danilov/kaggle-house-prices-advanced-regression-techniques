# from pandas import (
#     # Index,
#     MultiIndex,
# )

var_type = None

transformers = [
    # lambda _: _.set_index(enumerate(_.index, 1)),
    # lambda _: _.set_index(
    #     Index(
    #         data=enumerate(_.index, 1),
    #         name=('', 'variable'),
    #     ),
    # ),
    # lambda _: _.set_index(
    #     MultiIndex.from_tuples(
    #         tuples=enumerate(_.index, 1),
    #         names=('', 'variable')
    #     )
    # ),
]
