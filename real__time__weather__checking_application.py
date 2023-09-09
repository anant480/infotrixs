import requests
import json
import time
from datetime import datetime

API_KEY = "6145331e14ee162d3f6e19294de8c16d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    
    params = {'q': city_name, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print("Error: Unable to fetch weather data.")
        return None

def main():
    while True:
        print("Weather Checking Application")
        print("1. Check Weather by City Name")
        print("2. Add City to Favorites")
        print("3. Remove City from Favorites")
        print("4. View Favorites")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter the city name: ")
            weather_data = get_weather(city_name)
            if weather_data:

                temp_city = weather_data['main']['temp']
                weather_desc = weather_data['weather'][0]['description']
                hmdt = weather_data['main']['humidity']
                wind_spd = weather_data['wind']['speed']
                date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

                print("-------------------------------------------------------------")
                print("Weather Stats for - {}  || {}".format(city_name.upper(), date_time))
                print("-------------------------------------------------------------")

                print("Current temperature is: {:.2f} deg C".format(temp_city))
                print("Current weather desc  :", weather_desc)
                print("Current Humidity      :", hmdt, '%')
                print("Current wind speed    :", wind_spd, 'kmph')
        elif choice == "2":
            # Implement Add City to Favorites
            pass
        elif choice == "3":
            # Implement Remove City from Favorites
            pass
        elif choice == "4":
            # Implement View Favorites
            pass
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(15 + 15 * (hash(city_name) % 4))

if __name__ == "__main__":
    main()