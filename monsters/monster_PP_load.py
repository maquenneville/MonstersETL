# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 00:21:37 2022

@author: marca
"""

import pandas as pd
import os
from pandasPostgresHelpersMonster import connect_and_load
import shutil
import time
import sys


if len(sys.argv) < 2:
    pass

else:
    args = sys.argv
    home_folder = args[1]


def monster_loader(folder):
    home_folder = folder + "\monsters"
    orig = folder + "\monsters\monsters\spiders"

    os.chdir(orig)

    file = "monsters.csv"

    if file in os.listdir(orig):

        shutil.copy(orig + f"\{file}", home_folder + f"\{file}")

        time.sleep(1)

        os.unlink(orig + f"\{file}")

        time.sleep(1)

        print(f"{file} copied to home folder, ready to load")

    os.chdir(home_folder)

    monsters = pd.read_csv(file)

    monsters = monsters.drop(
        monsters.index[monsters["name"] == "ACTIONS"]
    ).reset_index()

    monsters.rename(
        columns={
            "info": "infor",
            "cimmun": "condImmunity",
            "dimmun": "damImmunity",
            "res": "damResist",
            "dvuln": "damVuln",
        },
        inplace=True,
    )

    monsters = monsters.dropna(subset=["infor"]).reset_index()
    monsters.drop(monsters.columns[0], axis=1, inplace=True)

    monsters["languages"] = monsters.languages.replace(to_replace="â€”", value=None)

    del monsters["infor"]

    connect_and_load("monsters", monsters, home_folder)


monster_loader(home_folder)
