import requests

api_key = "3acdb467443244aba82144239242409"
def get_weather(city_name):
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        location = data['location']['name']
        temp = data['current']['temp_c']
        condition = data['current']['condition']['text']
        return f"Wetter in {location}: {temp}°C, {condition}."
    else:
        return "Stadt nicht gefunden oder API-Fehler."
