from pandas import DataFrame


def info(data: DataFrame):
    data.info(verbose=True)
