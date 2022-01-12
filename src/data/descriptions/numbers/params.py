from numpy import number

dtype = number

transformers = [
    lambda _: _.transpose(),
    lambda _: _.rename_axis('variable', axis='index'),
]
