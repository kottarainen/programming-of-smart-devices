import json

users_merged = {}

with open('users1.json') as file1:
    data1 = json.load(file1)
    users_merged.update(data1['table']['users'])

with open('users2.json') as file2:
    data2 = json.load(file2)
    users_merged.update(data2['table']['users'])

list_merged = list(users_merged.values())

with open('users.json', 'w') as f:
    json.dump(list_merged, f, indent=4)