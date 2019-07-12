import pyowm

owm = pyowm.OWM('eca2a54f90ef045064284de909dad028')
observation = owm.weather_at_place("Sao bernardo do campo,br")
w = observation.get_weather()
temperature = w.get_temperature('celsius')
print(temperature)