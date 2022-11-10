# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 02:11:39 2022

@author: marca
"""

import pandas as pd
import os
import shutil
import time


def move_csv_to_public(path):
    """


    Parameters
    ----------
    path : string, path of csv

    Returns
    -------
    None, moves csv file to Public for easy loading into Postgres

    """

    file = os.path.basename(path)

    os.replace(path, r"C:\Users\Public" + f"\{file}")

    time.sleep(5)

    print("file moved to public, ready to load")


def move_csv_to_proper(desPath):
    """


    Parameters
    ----------
    desPath : string, desired destination path for csv from Public

    Returns
    -------
    None, moves csv file from Public back to desired folder

    """

    file = os.path.basename(desPath)

    os.replace(r"C:\Users\Public" + f"\{file}", desPath)

    time.sleep(5)

    print("file moved from Public back to it's home")


def make_create_statement(tableName, dframe):
    """


    Parameters
    ----------
    tableName : string, name of desired table in Postgres
    dframe : Dataframe, the target pandas Dataframe

    Returns
    -------
    a SQL CREATE TABLE statement with the appropriate column names and data types.
    Note: you will need to designate PRIMARY KEYS and REFERENCE columns manually

    """

    colnames = list(dframe.columns)
    datatypes = list(dframe.dtypes)
    datatypes = [str(i) for i in datatypes]

    coldata = dict(zip(colnames, datatypes))

    sql = f"""
CREATE TABLE {tableName} (
                """

    for col, typ in coldata.items():
        snippet = ""
        snippet += col + " "
        if typ == "int64":
            snippet += "INTEGER,\n"
        elif typ == "object":
            snippet += "VARCHAR(200),\n"
        elif typ == "float64":
            snippet += "REAL,\n"

        sql += snippet
    sql = sql[:-2]
    sql += "\n);"

    return sql


def make_load_statement(tableName, dframe, fileName, folder):
    """


    Parameters
    ----------
    tableName : string, name of table being populated
    dframe : Dataframe, pandas Dataframe that was exported into the csv
    fileName : string, file name (plus .csv)
    folder: Main path to folder with CSVs, include r at beginning of string

    Returns
    -------
    a SQL COPY statement to load data from a csv file into a Postgres table

    """
    sql = f"COPY {tableName}("
    columns = list(dframe.columns)
    path = folder + f"\{fileName}"
    for n, i in enumerate(columns):
        if n == len(columns) - 1:
            sql += i + ")\n"
        else:
            sql += i + ","
    sql += f"FROM '{path}'\n"
    sql += """DELIMITER ','
CSV HEADER;
"""
    return sql
