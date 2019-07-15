import pyowm

owm = pyowm.OWM('911f5d4e3775dd19dad4fe18c959af1a')
observation = owm.weather_at_place('Koforidua, GH')
w = observation.get_weather()

print(w.get_wind())
print(w.get_humidity())
print(w.get_temperature())

