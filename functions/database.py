import os
import json

from classes import FlatInfo, OwnerInfo


DATA_DIRECTORY = "./data"
TABLE_ONE_FILE_PATH = "./data/table1.json"
TABLE_TWO_FILE_PATH = "./data/table2.json"


def load_tables() -> tuple[dict[str, FlatInfo], dict[str, OwnerInfo]]:
    table_one = dict()
    table_two = dict()

    if not os.path.exists(DATA_DIRECTORY):
        os.mkdir(DATA_DIRECTORY)

    if not os.path.exists(TABLE_ONE_FILE_PATH):
        with open(TABLE_ONE_FILE_PATH, "w") as fw:
            fw.write("{}")
    else:
        with open(TABLE_ONE_FILE_PATH, "r") as fr:
            table_one = json.loads(fr.read())

    if not os.path.exists(TABLE_TWO_FILE_PATH):
        with open(TABLE_TWO_FILE_PATH, "w") as fw:
            fw.write("{}")
    else:
        with open(TABLE_TWO_FILE_PATH, "r") as fr:
            table_two = json.loads(fr.read())

    return (flat_info_as_class_value(table_one), owner_info_as_class_value(table_two))


def write_tables(table_one: dict[str, FlatInfo], table_two: dict[str, OwnerInfo]):
    with open(TABLE_ONE_FILE_PATH, "w") as fw:
        fw.write(json.dumps(as_dict_value(table_one), indent=4))

    with open(TABLE_TWO_FILE_PATH, "w") as fw:
        fw.write(json.dumps(as_dict_value(table_two), indent=4))


def as_dict_value(table: dict[str, FlatInfo] | dict[str, OwnerInfo]) -> dict:
    dict_copy = {}

    for i in table:
        dict_copy[i] = table[i].to_dict()

    return dict_copy


def flat_info_as_class_value(table: dict) -> dict[str, FlatInfo]:
    dict_copy = {}

    for i in table:
        dict_copy[i] = FlatInfo.from_dict(table[i])

    return dict_copy


def owner_info_as_class_value(table: dict) -> dict[str, OwnerInfo]:
    dict_copy = {}

    for i in table:
        dict_copy[i] = OwnerInfo.from_dict(table[i])

    return dict_copy
