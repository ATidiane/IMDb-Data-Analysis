#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime


def delete_columns(data, columns_to_drop):
    """ Delete specified columns in columns_to_drop from the dataframe
    :param data: dataframe from which to delete columns
    :param columns_to_drop: list of columns to delete
    :returns: a dataframe
    :rtype: pandas.DataFrame
    """

    for column in columns_to_drop:
        if column in data.columns:
            data.drop(column, axis=1, inplace=True)

    return data


def transform_date(x):
    """FIXME! briefly describe function

    :param x:
    :returns:
    :rtype:

    """

    try:
        return datetime.strptime(x, '%Y-%m-%d').year
    except BaseException:
        try:
            return int(x)
        except BaseException:
            return 0
