import requests
import json

API_KEY = "fgncLWJrtrS5Ua0fDM5zmXrTBubK9rPY"

LOCATION = "266850"

DAILY_FORECAST_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+LOCATION + "?apikey=" + API_KEY + "&language=pl-PL&metric=true"

r = requests.get(DAILY_FORECAST_URL)

jsonedResponse = json.loads(r.text)
print('[{"description":"' + jsonedResponse["Headline"]["Text"] + '","minTemp":"' + str(jsonedResponse["DailyForecasts"][0]["Temperature"]["Minimum"]["Value"]) + '","maxTemp":"'+ str(jsonedResponse["DailyForecasts"][0]["Temperature"]["Maximum"]["Value"]) + '"}]')

