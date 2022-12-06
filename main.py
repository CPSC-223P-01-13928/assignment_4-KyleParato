import weather
import json

filename = ""
weather_data = {}

choice = 0

menu = "        *** TUFFY TITAN WEATHER LOGGER MAIN MENU\n"
menu += """1. Set data filename\n
	2. Add weather data\n
	3. Print daily report\n
	4. Print historical report\n
	9. Exit the program\n"""
while choice != 9:
    choice = int(input("Enter menu choice: "))
    if(choice == 1):
        filename = str(input("Enter data filename: "))
        weather.read_data(filename)
        json.dump(weather_data,filename)
    if(choice == 2):
        datetime = str(input("Enter date (YYYYMMDD): "))
        datetime += str(input("Enter time (hhmmss): "))
        temp = int(input("Enter temperature: "))
        hum = int(input("Enter humidity: "))
        rain = float(input("Enter rainfall: "))
        weather_data[datetime]["t"] = temp
        weather_data[datetime]["h"] = hum
        weather_data[datetime]["r"] = rain
        weather.write_data(weather_data,filename)
    if(choice == 3):
        date = str(input("Enter date (YYYYMMDD): "))
        weather.report_daily(weather_data, filename)
    if(choice == 4):
        weather.report_historic(weather_data)
    if(choice == 9):
        break