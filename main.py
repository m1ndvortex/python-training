dict1 = {
    'value1': 10,
}
dict2 = dict1.copy()
print(dict1, id(dict1))
print(dict2, id(dict2))

dict2['value1'] = 20
print(dict1, id(dict1))
print(dict2, id(dict2))