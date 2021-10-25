from weather_model import WeatherModel
import requests


def callWeathApi():
    url = "http://openapi.seoul.go.kr:8088/6d424f64706765743730746d476f47/json/RealtimeCityAir/1/5?END_INDEX=1"
    response = requests.get(url)

    responseDict = response.json()  # 딕셔너리 타입으로 변환
    weather = responseDict["RealtimeCityAir"]["row"]  # list타입

    return weather
