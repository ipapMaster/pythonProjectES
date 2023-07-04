import requests  # библиотека для http-запросов
from datetime import datetime

town = input('Введите город: ')

key = 'c747bf84924be997ff13ac5034fa3f86'
url = 'http://api.openweathermap.org/data/2.5/weather'
params = {'APPID': key, 'q': town, 'units': 'metric'}

request = requests.get(url, params=params)

result = request.json()
print(result['main']['feels_like'])
code = result['cod']

if code != '401':
    if code != '404':
        data = result['main']
        print(f'Температура: {data["temp"]:.1f}\xB0C')
        print('Влажность', data['humidity'], '%')
        raw_time_sunset = result['sys']['sunset']
        print('Закат:', datetime.utcfromtimestamp(raw_time_sunset).strftime("%H:%M"))
        print(f'Координаты: {result["coord"]["lon"]}, {result["coord"]["lat"]}')
        if result['weather'][0]['main'] == 'Clouds':
            print('Облачно')
else:
    print('Информации нет!')
