import json  # Java Script Object Notation

with open('pets.json') as pet_file:
    data = json.load(pet_file)

for item in data:
    if type(data[item]) == list:
        print(item, ', '.join(data[item]))
    elif type(data[item]) == dict:
        print(item)
        for k, v in data[item].items():
            print(k, v)
    else:
        print(item, data[item])
