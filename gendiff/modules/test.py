dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
dict2 = {
    'c': 3,
    'd': 4,
    'e': 5
}

set1 = set(dict1)
set2 = set(dict2)

union = set1.union(set2)
intersection = set1.intersection(set2)
difference = set1.difference(set2)
symmetric_difference = set1.symmetric_difference(set2)
print(f'union is: {union}')
print(f'intersection is: {intersection}')
print(f'difference is: {difference}')
print(f'symmetric_difference is: {symmetric_difference}')
print(list(set2))
print(sorted(list(set2)))