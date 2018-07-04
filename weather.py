import requests

class Weather():
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def getFiveDay(self):
        response = requests.get("http://api.openweathermap.org/data/2.5/forecast?q=" + self.city + "," + self.country + "&APPID=c9c6113f1f5f3cdded7bc6b740864663&units=imperial")
        data = response.json()
        if data['cod'] == '404':
            return None
        count = data['cnt']
        weatherList = data['list']
        fiveDay = []
        tempMin = weatherList[0]['main']['temp']
        tempMax = weatherList[0]['main']['temp']
        for i in range(count):
            time = weatherList[i]['dt_txt']
            mainData = weatherList[i]['main']
            if i != 0 and time.split(" ")[1] == "00:00:00":
                fiveDay.append([tempMin, tempMax])
                tempMax = mainData['temp']
                tempMin = mainData['temp']
            else:
                currWeather = mainData['temp']
                if(currWeather > tempMax):
                    tempMax = currWeather
                if(currWeather < tempMin):
                    tempMin = currWeather
        fiveDay.append([tempMin, tempMax])
        return fiveDay
