# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from monsters.items import MonstersItem
import pandas as pd
import re


class MonstersPipeline:
    def process_item(self, item, spider):

        monster = item

        num_re = re.compile("^\d+$")

        if monster["info"]:
            monster["info"] = monster["info"].split("\n")
            info_cleaned = []

            for s in monster["info"]:
                if s != "":
                    info_cleaned.append(s)
                    if "Hit Points" in s:
                        monster["HP"] = s.split(" ")[2]
                        if not num_re.match(monster["HP"]):
                            monster["HP"] = None
                        else:
                            monster["HP"] = int(monster["HP"])
                    if "Speed" in s:
                        monster["speed"] = " ".join(s.split(" ")[1:])
                    if "Armor" in s:
                        monster["AC"] = s.split(" ")[2]
                        if not num_re.match(monster["AC"]):
                            monster["AC"] = None
                        else:
                            monster["AC"] = int(monster["AC"])
                    if "Languages" in s:
                        monster["languages"] = " ".join(s.split(" ")[1:])

                    if "Challenge" in s:
                        monster["chall"] = int(s.split(" ")[1])
                    if "Damage Resistances" in s:
                        monster["res"] = s.split("Damage Resistances ")[-1]
                        if "Damage Immunities" in monster["res"]:
                            monster["res"] = monster["res"].split("Damage Immunities")[
                                0
                            ]
                        if "Condition Immunities" in monster["res"]:
                            monster["res"] = monster["res"].split(
                                "Condition Immunities"
                            )[0]
                    if "Senses" in s:
                        monster["senses"] = " ".join(s.split(" ")[1:])
                        if "passive Perception" in monster["senses"]:
                            monster["senses"] = monster["senses"].split("passive")[0]

                    if "Condition Immunities" in s:
                        monster["cimmun"] = s.split("Condition Immunities ")[-1]
                    if "Damage Immunities" in s:
                        monster["dimmun"] = s.split("Damage Immunities ")[-1]
                        if "Condition Immunities" in monster["dimmun"]:
                            monster["dimmun"] = monster["dimmun"].split(
                                "Condition Immunities"
                            )[0]
                    if "Damage Vulnerabilities" in s:
                        monster["dvuln"] = s.split("Damage Vulnerabilities ")[-1]
                        if "Damage Immunities" in monster["dvuln"]:
                            monster["dvuln"] = monster["dvuln"].split(
                                "Damage Immunities"
                            )[0]
                        if "Condition Immunities" in monster["dvuln"]:
                            monster["dvuln"] = monster["dvuln"].split(
                                "Condition Immunities"
                            )[0]
                        if "Damage Resistances" in monster["dvuln"]:
                            monster["dvuln"] = monster["dvuln"].split(
                                "Damage Resistances"
                            )[0]

            monster["info"] = info_cleaned

            basic = info_cleaned[0].split(" ")

            monster["Str"] = monster["info"][10]
            monster["Dex"] = monster["info"][11]
            monster["Con"] = monster["info"][12]
            monster["Int"] = monster["info"][13]
            monster["Wis"] = monster["info"][14]
            monster["Cha"] = monster["info"][15]

            monster["size"] = basic[0]
            monster["Type"] = basic[1].strip(",")
            monster["alignment"] = " ".join([basic[-2], basic[-1]])

        return monster
