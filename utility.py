import pandas as pd


def drop_col(df: pd.DataFrame, col: str):
    return df.loc[:, df.columns != col]


def subtract_lists(list1: list, list2: list):
    """
    removes list of items from other list of items
    items that are in list2 will be removed from list1
    """
    return list(set(list1) - set(list2))
