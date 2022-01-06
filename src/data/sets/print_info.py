from pandas import DataFrame


def print_info(data_set: DataFrame):
    data_set.info(verbose=True)
