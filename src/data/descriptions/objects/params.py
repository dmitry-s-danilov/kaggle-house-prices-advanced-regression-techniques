dtype = object

transformers = [
    lambda _: _.transpose(),
    lambda _: _.rename_axis(
        mapper='variable',
        axis='index'
    ),
]
