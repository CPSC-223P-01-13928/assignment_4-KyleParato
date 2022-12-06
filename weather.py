import json
from calendar import month_name

def read_data(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def write_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def max_temperature(data, date):
    max = -9999999
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] > max:
                max = data[key]['t']
    return max 
def min_temperature(data, date):
    min = 99999999
    for key in data:
        if date == key[0:8]:
            if data[key]['t'] < min:
                min = data[key]['t']
    return min 

def max_humidity(data, date):
    max = -999999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] > max:
                max = data[key]['h']
    return max

def min_humidity(data, date):
    min = 99999999
    for key in data:
        if date == key[0:8]:
            if data[key]['h'] < min:
                min = data[key]['h']
    return min 

def tot_rain(data, date):
    sum = 0
    for key in data:
        if(date == key[0:8]):
            sum += data[key]['r']
    return sum

def report_daily(data, date):
    to_display = "========================= DAILY REPORT ========================\n"
    to_display += "Date                      Time  Temperature  Humidity  Rainfall\n"
    to_display += "====================  ========  ===========  ========  ========\n"
    
    date_display = (month_name[int(date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4])) + "      ")
    for key in data:
        if(date == key[0:8]):
            to_display += (date_display + str((key[8:10])) + ":" + str((key[10:12])) + ":" + str((key[12:14]))+"           " + str(data[key]['t']) + "        " + str(data[key]['h'])
                           + "      " + str(data[key]['r']) +  "\n")
    
    
    return to_display

def report_historical(data):
    to_display  = "============================== HISTORICAL REPORT ===========================\n"
    to_display += "                          Minimum      Maximum   Minumum   Maximum     Total\n"
    to_display += "Date                  Temperature  Temperature  Humidity  Humidity  Rainfall\n"
    to_display += "====================  ===========  ===========  ========  ========  ========\n"

    uniqueDates = []
    for key in data:
        if key[0:8] not in uniqueDates:
            uniqueDates.append(key[0:8])
    
    for date in uniqueDates:
        to_display += (month_name[int(date[4:6])] + " " + str(int(date[6:8])) + ", " + str(int(date[0:4])))
        mint = min_temperature(data,date)
        maxt = max_temperature(data,date)
        minh = min_humidity(data,date)
        maxh = max_humidity(data,date)
        rain = tot_rain(data,date)
        to_display += f'{mint:17}{maxt:13}{minh:10}{maxh:10}{rain:10.2f}' + "\n"
    
    return to_display
