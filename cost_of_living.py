import os
import requests
from geopy.geocoders import Nominatim

city = 'Minneapolis'
state_code = 'MN'
key = os.environ.get('COST_OF_LIVING_KEY')
url = f'https://www.numbeo.com//api/city_cost_estimator?api_key={key}&query={city},%20{state_code},%20United%20States&members=1&children=0&include_rent=true&currency=USD'
data = requests.get(url).json()
def get_cost_of_living(city, state_code):
    pass

cost_of_living = data.get('overall_estimate')

print('{:.2f}'.format(cost_of_living))