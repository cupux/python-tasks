import pyowm

location = input("Enter your location: ")
def weather(location):
    
    owm = pyowm.OWM('911f5d4e3775dd19dad4fe18c959af1a')
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    w.get_wind()
    w.get_humidity()
    return w.get_temperature()

print(weather(location))

