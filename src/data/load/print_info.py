from pandas import DataFrame


def print_info(data: DataFrame):
    data.info(verbose=True)
