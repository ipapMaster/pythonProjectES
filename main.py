import json  # Java Script Object Notation

weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг',
            'Пятница', 'Суббота', 'Воскресенье']


week_dict = {key: val for key, val in enumerate(weekdays)}

data = json.dumps(week_dict)

print(data)
