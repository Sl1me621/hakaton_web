import requests
r=requests.get('http://export.yandex.ru/weather-ng/forecasts/192').json()
print(r)
