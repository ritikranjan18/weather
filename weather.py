import requests

def get_weather(city):
    API_KEY = "3125066be52622b546c5a7d577fa385d"  # Replace with your OpenWeatherMap API key
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    # Request parameters
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # For temperature in Celsius
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        print(f"\n📍 Weather in {city.capitalize()}")
        print(f"🌡️ Temperature: {main['temp']}°C")
        print(f"💧 Humidity: {main['humidity']}%")
        print(f"🔎 Description: {weather['description'].capitalize()}")
    else:
        print("❌ City not found. Please check the spelling.")

# Main Program
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
