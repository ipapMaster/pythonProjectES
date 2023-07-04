import json  # Java Script Object Notation

pets = {
    'name': 'Barsik',
    'age': 12,
    'meals': ['Purina', 'Wiskas'],
    'owner': {'fname': 'John', 'sname': 'Smith'}
}

with open('pets.json', 'w') as pet_file:
    json.dump(pets, pet_file)
