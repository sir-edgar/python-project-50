import json
from gendiff.modules.parser import parser


def generate_diff(file_path1, file_path2):
    set1, set2, dict1, dict2 = parser(file_path1, file_path2)
    sorted_union = sorted(list(set1.union(set2)))
    result = '{\n'
    for key in sorted_union:
        if key in dict1 and key in dict2:
            if dict1.get(key) == dict2.get(key):
                result = result + f'    {key}: {str(dict1.get(key))}' + '\n'
            else:
                result = result + f'  - {key}: {str(dict1.get(key))}' + '\n'
                result = result + f'  + {key}: {str(dict2.get(key))}' + '\n'
        elif key in dict1 or key in dict2:
            if key in dict1:
                result = result + f'  - {key}: {str(dict1.get(key))}' + '\n'
            else:
                result = result + f'  + {key}: {dict2[key]}' + '\n'
    return result + '}'
