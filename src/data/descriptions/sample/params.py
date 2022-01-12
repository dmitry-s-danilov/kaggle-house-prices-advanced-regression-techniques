n = (3, 6, 3)

transformers = [
    lambda _: _.transpose(),

    lambda _: _.rename_axis(
        mapper='variable',
        axis='index',
    ),
    lambda _: _.rename_axis(
        mapper='id',
        axis='columns',
    ),
]
