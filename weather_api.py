import requests, json
import datetime as dt


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "City of Zagreb, HR"
API_KEY = ""
URL = BASE_URL + "q=" + CITY + "&units=metric&appid=" + API_KEY

# &units=metric for metric units

def weather_data():
   response = requests.get(URL)

   if response.status_code == 200:

      data = response.json()

      time = dt.datetime.now().strftime("%H:%M:%S")

      icon = data["weather"][0]["icon"]

      main = data['main']

      temperature = main['temp']

      humidity = main['humidity']

      pressure = main['pressure']

      report = data['weather']
      dict = {
         "CITY": CITY, 
              "time": time, 
              "icon": icon, 
              "main": main, 
              "temp": temperature, 
              "humidity": humidity, 
              "pressure": pressure,
              "report": report
              }

      with open("weather.json", "a") as f:
         json.dump(dict, f, indent=4)
         
      print(f"{CITY:-^30}")
      print(time)
      print(f"http://openweathermap.org/img/wn/{icon}.png") #icon
      print(f"Temperature: {temperature}°C")
      print(f"Humidity: {humidity}%")
      print(f"Pressure: {pressure}pa")
      print(f"Weather Report: {report[0]['description']}")
   
   else:
      print("Error in the HTTP request")


weather_data() 