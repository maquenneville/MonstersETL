# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 00:21:37 2022

@author: marca
"""

import pandas as pd
import os
import psycopg2
from config import config
from pandasPostgresHelpersMonster import connect_and_load
import shutil
import time

orig = r"C:\Users\marca\Desktop\Coding\PythonWork\WebScraping\monsters\monsters\spiders"

home_folder = r"C:\Users\marca\Desktop\Coding\PythonWork\WebScraping\monsters"

os.chdir(orig)


file = "monsters.csv"

shutil.copy(orig + f"\{file}", home_folder + f"\{file}")

time.sleep(2)

print(f"{file} copied to home folder, ready to load")


os.chdir(home_folder)

csv = "monsters.csv"

monsters = pd.read_csv(csv)

monsters = monsters.drop(monsters.index[monsters["name"] == "ACTIONS"]).reset_index()

monsters.rename(columns={"info": "infor"}, inplace=True)

monsters = monsters.dropna(subset=["infor"]).reset_index()
monsters.drop(monsters.columns[0], axis=1, inplace=True)

monsters["languages"] = monsters.languages.replace(to_replace="â€”", value=None)

del monsters["infor"]


connect_and_load("monsters", monsters, home_folder)
