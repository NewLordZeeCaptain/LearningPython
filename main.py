from pprint import pprint
from config import open_weather_token
import requests
import datetime

def get_weather (city,open_weather_token):

    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric&lang=ru'
        )
        data = r.json()
        # pprint(data)

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Сам посмотри"

        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        print(f"Сегодня: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
              f"Погода в городе: {city}\n"
              f"Температура: {cur_weather} {wd}\n"
              f"Влажность: {humidity}\n"
              f"Давление: {pressure}\n"
              f"Скорость ветра: {wind}\n"
              f"Время восхода: {sunrise_timestamp}\n"
              f"Время заката: {sunset_timestamp}\n"
              f"Продолжительность часового дня: {length_of_the_day}")



    except Exception as ex:
        print(ex)
        print("Неверное название города")

def main():
    city = input("Введите город: ")
    get_weather(city,open_weather_token)

if __name__ == '__main__':
    main()