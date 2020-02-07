import requests # Need to install requests as it is not part of the standard library
from datetime import datetime
import csv

API_KEY = 'Your EIA API Key' # Replace with your own API Key 
SERIES_ID_DAY = 'NG.RNGWHHD.D'
SERIES_ID_WEEK = 'NG.RNGWHHD.W'
SERIES_ID_MONTH = 'NG.RNGWHHD.M'
SERIES_ID_YEAR = 'NG.RNGWHHD.A'


def setParameters(series_id):
    parameters = {
        'api_key': API_KEY,
        'series_id': series_id
    }
    return parameters


def getPrices(series_id, outputfilename):
    response = requests.get('http://api.eia.gov/series/',params=setParameters(series_id))
    data = response.json()['series'][0]['data'] # data is list with list of days and price
    
    with open(outputfilename,"w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerow(['Date','Price']) # Adding column headers
        for item in data:
            if (len(item[0]) == 8):
                item[0] = datetime.strptime(item[0], '%Y%m%d').date() # Convert all the first items to datetime and only take date for csv
            elif (len(item[0]) == 6):
                item[0] = datetime.strptime(item[0], '%Y%m').date()
            writer.writerow(item) # Write data to csv

getPrices(SERIES_ID_DAY,'days_price.csv')
getPrices(SERIES_ID_WEEK,'weeks_price.csv')
getPrices(SERIES_ID_MONTH, 'months_price.csv')
getPrices(SERIES_ID_YEAR, 'years_price.csv')