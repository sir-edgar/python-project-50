import json
import yaml


def parser(file_path1, file_path2):
    if file_path1[-4:] == 'json':
        dict1 = json.load(open(file_path1))
        set1 = set(dict1)
    elif file_path1[-4:] == 'yaml' or file_path1[-3:] == 'yml':
        with open(file_path1, 'r') as file:
            dict1 = yaml.safe_load(file)
            set1 = set(dict1)
    if file_path2[-4:] == 'json':
        dict2 = json.load(open(file_path2))
        set2 = set(dict2)
    elif file_path2[-4:] == 'yaml' or file_path1[-3:] == 'yml':
        with open(file_path2, 'r') as file:
            dict2 = yaml.safe_load(file)
            set2 = set(dict2)
    return set1, set2, dict1, dict2
