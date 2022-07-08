from weather4py import __version__
from weather4py import WeatherMan

def test_version():
    assert __version__ == '0.1.0'

def test_humidity():
    assert WeatherMan("israel").region == "Tel Aviv-Yafo, Israel"

def test_weather():
    assert WeatherMan("london").weather == "Sunny"

def test_temperature():
    assert WeatherMan("texas").temperature == int(30)

def test_humidity():
    assert WeatherMan("israel").humidity == "56%"