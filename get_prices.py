import requests # Need to install requests as it is not part of the standard library
from datetime import datetime
import csv

API_KEY = 'EIA API Key' # Replace with your own API Key 
SERIES_ID = 'NG.RNGWHHD.D'

parameters = {
	'api_key': API_KEY,
	'series_id': SERIES_ID
}

response = requests.get('http://api.eia.gov/series/',params=parameters)
data = response.json()['series'][0]['data'] # data is list with list of days and price

with open("days_price.csv","w") as output:
	writer = csv.writer(output, lineterminator='\n')
	writer.writerow(['Date','Price']) # Adding column headers
	for item in data:
	    item[0] = datetime.strptime(item[0], '%Y%m%d').date() # Convert all the first items to datetime and only take date for csv
	    writer.writerow(item) # Write data to csv
