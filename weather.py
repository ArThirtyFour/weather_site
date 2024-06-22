import requests 
from googletrans import Translator

def weather_city(city):
  try:
    itogi = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={da}&appid=adbb2821feabdbc9583b52bec964c8c1').json()
    city = translator.translate(itogi['name'], dest="ru")
    weather = translator.translate(itogi['weather'][0]['description'], dest="ru")
    temperature = round(float(itogi['main']['temp'] - 273.0 ),2)
    return city.text , weather , temperature.text[0]+weather.text[1:]
  except:
        return None
